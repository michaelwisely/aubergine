BROKER_URL = 'mongodb://127.0.0.1/celery'

CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1/celery_results'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'auth'
CELERY_ACCEPT_CONTENT = ['json', 'auth']
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Should be set in secret_settings.py
# CELERY_SECURITY_KEY = ""
# CELERY_SECURITY_CERTIFICATE = ""
# CELERY_SECURITY_CERT_STORE = ""
