from datetime import timezone
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

celery_app = Celery('main_app')
celery_app.conf.enable_utc = False
celery_app.conf.update(timezone='Asia/Kolkata')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# celery beat
celery_app.conf.beat_schedule = {

    'send-mail-everyday-at-12' : {
        'task': 'send_mails_app.tasks.send_mail_func',
        'schedule': crontab(hour=13, minute=40),
        'args' : ()
    }

}


celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')