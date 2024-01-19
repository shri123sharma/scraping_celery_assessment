from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapper_project.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('scrapper_project')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'cron job':{
        'task': 'scrap.tasks.New_Func',
        'schedule' :crontab(minute=0, hour=0)
        
        
    }
}
