# coding:utf-8

from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'ptask': {
        'task': 'tasks.period_task',
        'schedule': timedelta(seconds=5),
    },
}

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'
