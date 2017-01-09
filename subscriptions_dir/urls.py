from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.subscriptions_dir, name='home'),
    url(r'^subscriptions/(?P<recipient_tag>.+)/$', views.subscriptions_dir_specific, name='subscriptions_dir_specific'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^$', views.subscriptions_dir, name='home'),
]
