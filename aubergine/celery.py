from __future__ import absolute_import

from celery import Celery


app = Celery('aubergine')
app.config_from_object('aubergine.settings.celeryconfig')
app.autodiscover_tasks(['aubergine'], related_name='tasks')

# For message signing
# app.setup_security()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task()
def tadd(x, y):
    return x + y


@app.task()
def tsum(numbers):
    return sum(numbers)
