from importlib import import_module

from django.apps import AppConfig


class SubscriptionsDirConfig(AppConfig):
    name = 'subscriptions_dir'

    def ready(self):
        import_module("subscription_dir.receivers") 