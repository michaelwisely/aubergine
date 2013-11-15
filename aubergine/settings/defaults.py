import os
from django.contrib import messages

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)
BUILDOUT_DIR = os.path.dirname(PROJECT_DIR)
VAR_DIR = os.path.join(BUILDOUT_DIR, "var")

##########################################################################
#
# Secret settings
#
##########################################################################
# If a secret_settings file isn't defined, open a new one and save a
# SECRET_KEY in it. Then import it. All passwords and other secret
# settings should be stored in secret_settings.py. NOT in settings.py
try:
    from secret_settings import *
except ImportError:
    print "Couldn't find secret_settings file. Creating a new one."
    secret_settings_loc = os.path.join(SETTINGS_DIR, "secret_settings.py")
    with open(secret_settings_loc, 'w') as secret_settings:
        secret_key = ''.join([chr(ord(x) % 90 + 33) for x in os.urandom(40)])
        secret_settings.write("SECRET_KEY = '''%s'''\n" % secret_key)
    from secret_settings import *

##########################################################################
#
# Administrative settings
#
##########################################################################

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


##########################################################################
#
#  Authentication settings
#
##########################################################################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


##########################################################################
#
# Crispy settings
#
##########################################################################

CRISPY_TEMPLATE_PACK = 'bootstrap'


##########################################################################
#
# Celery settings
#
##########################################################################
import djcelery
djcelery.setup_loader()

try:
    BROKER_URL
except NameError:
    BROKER_URL = 'django://'

CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


##########################################################################
#
# Testing settings
#
##########################################################################

# Sets the testrunner to Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


##########################################################################
#
# Messages settings
#
##########################################################################

# Change the default messgae tags to play nice with Bootstrap
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-error',
}


##########################################################################
#
# Database settings
#
##########################################################################

# Should be overridden by development.py or production.py
DATABASES = None

# Add project/fixtures to the list of places where django looks for
# fixtures to install.
FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, "fixtures"),
)


##########################################################################
#
# Cache settings
#
##########################################################################

CACHE_MIDDLEWARE_SECONDS = 5
CACHE_MIDDLEWARE_KEY_PREFIX = 'web_cache'


##########################################################################
#
# Location settings
#
##########################################################################

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = True


##########################################################################
#
# Static files settings
#
##########################################################################
MEDIA_ROOT = os.path.join(VAR_DIR, "uploads")
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_DIR, "static")
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


##########################################################################
#
# Template settings
#
##########################################################################

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    # for django-admin-tools and zinnia
    'django.core.context_processors.request',
)


##########################################################################
#
# Middleware settings
#
##########################################################################

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


##########################################################################
#
# URL settings
#
##########################################################################

ROOT_URLCONF = 'aubergine.urls'


##########################################################################
#
# Installed apps settings
#
##########################################################################

INSTALLED_APPS = (
    # Django Admin Tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # django-crispy-forms
    'crispy_forms',

    # Celery integration for Django
    'djcelery',
    'kombu.transport.django',

     # Adds gunicorn management commands
    'gunicorn',

    # Django client for Sentry (getsentry.com)
    'raven.contrib.django.raven_compat',

    # Additional management commands
    'django_extensions',

    # Nose test suite
    'django_nose',

    # South should be last
    'south'
)


##########################################################################
#
# Logging settings
#
##########################################################################

# Check development.py or production.py for specific logging settings.
LOGGING = None
