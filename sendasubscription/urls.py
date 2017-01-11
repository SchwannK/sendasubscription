from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r"", include('subscriptions_dir.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^faq/', include('faq.urls')),
    url(r'^contact/', views.contact, name='contact')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
