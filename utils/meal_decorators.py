from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from meal_order.models import Token

__author__ = 'allen.zhang'

def user_required(func):
    def wrapper(request,*args,**kwargs):
        token = request.session.get("token",None) if request.session.get("token",None) else request.GET.get("token",None)
        if not token:
            return HttpResponseRedirect(reverse("login"))
        token_obj = Token.objects.filter(token_string=token)
        if token_obj:
            token_obj = token_obj[0]
            user = token_obj.user
            request.user = user
            return func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("login"))
    return wrapper
