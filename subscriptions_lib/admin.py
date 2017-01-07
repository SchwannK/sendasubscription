from django.contrib import admin
from .models import Category, Company, Subscription

# Register your models here.
myModels = [Category, Company, Subscription]

admin.site.register(myModels)
