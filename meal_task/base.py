#coding=utf8
from django.core.mail import send_mail
import redis,json
from mongoengine import connect
from meal_order.models import *
connect("meal")
from threading import Timer

from django.conf import settings



task_run_frequency = settings.TASK_RUN_FREQUENCY


redis_pool = redis.ConnectionPool(host="localhost",port=6379,db=0)
redis_obj = redis.Redis(connection_pool=redis_pool)


class Task(object):
    def register(self,job_class,*args,**kwargs):
        job_instance = job_class()
        self.job_instance = job_class()

    def execute(self):
        try:
            self.job_instance.do_job()
        except:
            pass
        Timer(task_run_frequency,self.execute).start()



class Job(object):

    run_every = task_run_frequency

    def run(self, *args, **kwargs):
        self.do_job()

    def do_job(self):
        pass


class BillSendJob(Job):
    run_every = task_run_frequency
    def do_job(self):
        try:
            bill_info = json.loads(redis_obj.lpop("bill_queue"))
            restaurant_id = bill_info.keys()[0]
            restaurant = Restaurant.objects.get(id=restaurant_id)
            meal_id_list = bill_info[restaurant_id]
            meal_name = ','.join([food.name for food in Food.objects.filter(id__in=meal_id_list)])
            send_mail('You receive a bill', meal_name, 'yulong@conversant.com.cn',['%s' % restaurant.admin], fail_silently=False)
        except:
            pass

bill_task = Task()
bill_task.register(BillSendJob)
