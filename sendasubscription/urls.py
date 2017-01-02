from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'', include('subscriptions_dir.urls')),
    url(r'^contact/', views.contact, name='contact'),
    
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^payments/", include("pinax.stripe.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
