import cStringIO
import hashlib
from django.conf import settings
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from utils.meal_decorators import  *
from models import *
import datetime
from mongoengine import connect
connect("meal")

__author__ = 'allen.zhang'


class MealOrderBaseView(TemplateView):
    @method_decorator(user_required)
    def dispatch(self, *args, **kwargs):
        return super(MealOrderBaseView,self).dispatch(*args,**kwargs)


class LoginView(TemplateView):
    template_name = "login.html"
    def get(self, request, *args, **kwargs):
        c = self.get_context_data(**kwargs)
        return self.render_to_response(c)

    def post(self,*args,**kwargs):
        email = self.request.POST.get("email",None)
        password = self.request.POST.get("password",None)
        if email and password:
            user = User.objects.filter(email=email,password=password)
            if user:
                strbuf = cStringIO.StringIO()
                strbuf.write(email+datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                token = str(hashlib.sha512(strbuf.getvalue()).hexdigest())
                Token(user_id=str(user[0].id),token_string=token).save()
                self.request.session['token'] = token
                return HttpResponseRedirect(reverse("user"))
            return HttpResponse("user not found",status=200)
        return HttpResponse("invalid parameter",status=200)




class UserInfoView(MealOrderBaseView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        c = self.get_context_data(**kwargs)
        user_info = User.objects.filter(id=request.user.id).select_related()
        c['user_info'] = user_info
        return self.render_to_response(c)


class OrderView(MealOrderBaseView):
    template_name = 'restaurant.html'
    def get(self, request, *args, **kwargs):
        restaurant_id = request.GET.get("restaurant_id",None)
        c = self.get_context_data(**kwargs)
        if not restaurant_id:
            menu_info_list = Restaurant.objects
            c['menu_info_list'] = menu_info_list
        else:
            self.template_name = "menu.html"
            menu_info_list = Food.objects.filter(restaurant_id=restaurant_id).select_related()
            c['menu_info_list'] = menu_info_list
            c['status'] = settings.FOOD_ORDER_STATUS
            c['restaurant_id'] = restaurant_id
        return self.render_to_response(c)

    def post(self,*args,**kwargs):
        meal_id_list = self.request.POST.getlist("meal_id")
        restaurant_id = self.request.POST.get("restaurant_id")
        cost = self.request.POST.get("cost")
        if not meal_id_list:
            return HttpResponse("invalid parameter",status=200)

        new_bill = Bill()
        new_bill.user_id=str(self.request.user.id)
        food_id_list = []
        restaurant = Restaurant.objects.get(id=restaurant_id)
        restaurant.number = restaurant.number + 1
        restaurant.save()
        for meal_id in meal_id_list:
            food = Food.objects.get(id=meal_id)
            food_id_list.append(str(food.id))
            History(user_id=str(self.request.user.id),name=food.name,cost=food.price).save()
        new_bill.food_id_list = food_id_list
        new_bill.cost = cost
        new_bill.save()
        return HttpResponse("ok",status=200)


class BillView(MealOrderBaseView):
    template_name = "bill.html"
    def get(self, request, *args, **kwargs):
        c = self.get_context_data(**kwargs)
        bill_id = self.request.GET.get("bill_id",None)
        user = self.request.user
        if not bill_id:
            item_list = Bill.objects.filter(user_id=str(user.id)).order_by("-time")
            c['item_list'] = item_list
        else:
            self.template_name = "menu.html"
            bill = Bill.objects.get(id=bill_id)
            item_list = Food.objects.filter(id__in=bill.food_id_list)
            c['menu_info_list'] = item_list
            c['status'] = settings.ORDER_CHECK_STATUS
            c['cost'] = reduce(int.__add__,[item.price for item in item_list])
        return self.render_to_response(c)
