from celery import Celery
from django.conf import settings

celery_app = Celery("core")
celery_app.config_from_object(settings)
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
