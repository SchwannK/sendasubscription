from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    favicon = models.CharField(max_length=20)       # Font Awesome favicon

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
    category = models.ForeignKey(Category)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to = 'subscription_thumbnails/')
    reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name or self.reference

    def save(self, *args, **kwargs):

        self.category = self.company.category

        super(Subscription, self).save(*args, **kwargs)
