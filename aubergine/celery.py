from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


# Set up Aubergine development app
os.environ['DJANGO_SETTINGS_MODULE'] = 'aubergine.settings.defaults'

app = Celery('aubergine')
app.config_from_object('aubergine.settings.celeryconfig')
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')
app.setup_security()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task()
def tadd(x, y):
    return x + y

@app.task()
def tsum(numbers):
    return sum(numbers)
