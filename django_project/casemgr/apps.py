from django.apps import AppConfig


class App0Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "casemgr"

    def ready(self):
        import casemgr.signals
