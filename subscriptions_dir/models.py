from django.contrib.auth.models import User
from django.db import models

from subscriptions_lib.models import Subscription


class Customer(models.Model):
    user = models.ForeignKey(User)
    client_token = models.TextField(verbose_name=u'client token', max_length=500)
    payment_nonce = models.CharField(max_length=100, null=True, blank=True)
    customer_id = models.CharField(max_length=25, null=True, blank=True)
    payment_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name 

class Giftee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    """ To add address field (perhaps use 3rd party package?) """

    def __str__(self):
        return self.name or self.reference


# Global table for all orders
class Order(models.Model):
    user = models.ForeignKey(User)
    subscription = models.ForeignKey(Subscription)
    giftee = models.ForeignKey(Giftee, null=True, blank=True)
    payment_nonce = models.CharField(max_length=100, null=True, blank=True)
    txnid = models.CharField(max_length=25, null=True, blank=True)
    date_purchased = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)  # Null -> Order pending; set -> Order completed
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.name or self.reference
