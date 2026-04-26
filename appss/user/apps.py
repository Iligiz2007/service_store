from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'appss.user'
    def ready(self):
        import appss.user.signals