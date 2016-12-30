from django.db import models
from subscriptions_lib.models import Subscription

class Giftee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    """ To add address field (perhaps use 3rd party package?) """

    def __str__(self):
        return self.name or self.reference


# Table generated for each individual user
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

    """ To add attributes for payment methods """

    def __str__(self):
        return self.name or self.reference


# Global table for all orders
class Order(models.Model):
    """ To add attribute for User ID """

    subscription = models.ForeignKey(Subscription)
    giftee = models.ForeignKey(Giftee)
    payment_method = models.ForeignKey(PaymentMethod)
    date_purchased = models.DateTimeField()
    date_completed = models.DateTimeField()     # Null -> Order pending; set -> Order completed

    def __str__(self):
        return self.name or self.reference
