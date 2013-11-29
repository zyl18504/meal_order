#coding=utf8

import redis,json
from django.conf import settings
from threading import Timer
from operations import *





redis_pool = redis.ConnectionPool(host="localhost",port=6379,db=0)
redis_obj = redis.Redis(connection_pool=redis_pool)
task_run_frequency = settings.TASK_RUN_FREQUENCY

class Task(object):

    def do_job(self):
        pass




class BillSendTask(Task):
    def do_job(self):
        while 1:
            Timer(task_run_frequency,bill_send_operation).start()

bill_task = BillSendTask()
