from django.apps import AppConfig


class CasemgrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "casemgr"

    def ready(self):
        import casemgr.signals # noqa: F401
