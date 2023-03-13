from os import environ

from celery import Celery
from celery.schedules import crontab

from django.conf import settings


environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
app: Celery = Celery(
    'settings',
    broker=settings.CELERY_BROKER_URL,
    include=(
        'auths.tasks',
    )
)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'every-months': {
        'task': 'wtf',
        'schedule': crontab(minute='*/1')
    },
}
app.conf.timezone = 'UTC'