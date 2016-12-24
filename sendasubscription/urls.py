from django.contrib import admin
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('subscriptions_dir.urls')),
    url(r'^contact/', views.contact, name='contact')
]
