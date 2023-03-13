from settings.celery import app

from services import re_zero_count_service

@app.shared_task(name='wtf')
def update_count():
    re_zero_count_service()