# coding:utf-8

from __future__ import absolute_import
from celery.schedules import crontab

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'

CELERY_TIMEZONE = 'Asia/Shanghai'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-3-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=3),
        'args': (15, 16)
    },
    'pop-every-2-seconds': {
        'task': 'tasks.pop',
        'schedule': timedelta(seconds=3),
        'args': (19, 16)
    },

    'add-everyday-afternoon': {
        'task':'tasks.now_time',
        'schedule':crontab(minute="*"),
        'args': (8,9)
    },
}
