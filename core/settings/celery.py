from celery import Celery
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.main")

app = Celery()

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()
