from importlib import import_module

from django.apps import AppConfig


class SendasubscriptionConfig(AppConfig):
    name = 'sendasubscription'

    def ready(self):
        import_module("sendasubscription.receivers") 