from django.conf.urls.defaults import patterns, include, url
from meal_order.views import *
from meal_task.base import *
bill_task.execute()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', UserInfoView.as_view(), name='user'),
                       url(r'^login$', LoginView.as_view(), name='login'),
                       url(r'^user$', UserInfoView.as_view(), name='user'),
                       url(r'^order', OrderView.as_view(), name='order'),
                       url(r'^bill', BillView.as_view(), name='bill'),
    # Examples:
    # url(r'^$', 'meal_order.views.home', name='home'),
    # url(r'^meal_order/', include('meal_order.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
