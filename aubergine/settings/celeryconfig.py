import os
import sys

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)
BUILDOUT_DIR = os.path.dirname(PROJECT_DIR)
VAR_DIR = os.path.join(BUILDOUT_DIR, "var")



##########################################################################
#
# Broker settings
#
##########################################################################

BROKER_URL = 'mongodb://192.168.1.4/celery'


##########################################################################
#
# Results settings
#
##########################################################################

CELERY_RESULT_BACKEND = 'mongodb://192.168.1.4/celery_results'
CELERY_RESULT_SERIALIZER = 'json'


##########################################################################
#
# Task settings
#
##########################################################################

CELERY_TASK_SERIALIZER = 'json'


##########################################################################
#
# Worker settings
#
##########################################################################

CELERY_ACCEPT_CONTENT = ['json']


##########################################################################
#
# Beat settings
#
##########################################################################

CELERYBEAT_SCHEDULE_FILENAME = 'var/db/celery-schedule.db'


##########################################################################
#
# Security settings
#
##########################################################################

# Try to load CELERY_SECURITY_* settings from secret_settings.py. If
# they're not there, throw an error and exit.
try:
    if CELERY_TASK_SERIALIZER == 'auth':
        from secret_settings import CELERY_SECURITY_KEY
        from secret_settings import CELERY_SECURITY_CERTIFICATE
        from secret_settings import CELERY_SECURITY_CERT_STORE
except ImportError:
    sys.stderr.write("""
        Couldn't load CELERY_SECURITY_* settings from secret_settings.py.
        Check to be sure that the following settings are defined:

            CELERY_SECURITY_KEY
            CELERY_SECURITY_CERTIFICATE
            CELERY_SECURITY_CERT_STORE

        This may require generating some SSL keys and certificates.\n\n""")
    sys.exit(1)
