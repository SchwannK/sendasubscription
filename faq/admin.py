from django.contrib import admin
from .models import FaqCategory, FaqEntry

# Register your models here.
myModels = [FaqCategory, FaqEntry]

admin.site.register(myModels)
