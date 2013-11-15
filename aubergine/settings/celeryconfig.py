BROKER_URL = 'mongodb://127.0.0.1/celery'
CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1/celery_results'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
