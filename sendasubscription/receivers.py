from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in
from subscriptions_dir.models import Customer

# from pinax.stripe.actions import customers


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    print("user_logged_in")


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    print("password_changed")


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    print("user_login_attempt")


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    print("user_sign_up_attempt")


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    print("user_signed_up " + str(kwargs))
    user = kwargs['user']
    customer = Customer()
    customer.user = user
    customer.save()
#     customers.create(kwargs.get("user"))
