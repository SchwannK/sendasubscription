from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subscriptions_dir, name='subscriptions_dir')
]
