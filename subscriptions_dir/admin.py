from django.contrib import admin
from .models import *

# Register your models here.
myModels = [Category, Company, Subscription]

admin.site.register(myModels)
