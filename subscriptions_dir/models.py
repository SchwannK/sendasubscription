from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name or self.reference


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name or self.reference


class Subscription(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name or self.reference
