#coding=utf8
from django.core.mail import send_mail


def bill_send_operation():
    send_mail('test', 'test.', 'yulong@conversant.com.cn',['to@592280502.qq.com'], fail_silently=False)