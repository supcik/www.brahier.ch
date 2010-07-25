# Django settings for brahier project.

import os
#import logging
#import logging.handlers
#import string

VERSION = "0.1.0"

ADMINS = (
    ('Jacques Supcik', 'jacques@supcik.net'),
)

MANAGERS = ADMINS

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
SHARE = '../../share'
VAR = '../../var'

DATABASES = {
    'default': {
         # Add 'postgresql_psycopg2', 'postgresql', 'mysql',
         # 'sqlite3' or 'oracle'.
        'ENGINE'    : 'django.db.backends.sqlite3',
        'NAME'      : os.path.join(PROJECT_PATH, VAR, 'brahier.sqlite'),
        'USER'      : '',
        'PASSWORD'  : '',
        'HOST'      : '',
        'PORT'      : '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr_CH'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, SHARE, 'static')


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nf^_78$g0g_v1t7$dm^!b810f$u5quokl*0s^z@=e@hwv6v9ez'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "brahier.context_processors.version",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'brahier.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, SHARE, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'brahier.www',
)

if 'DJANGO_MODE' in os.environ and os.environ['DJANGO_MODE'] == 'PROD':
    DEBUG = False
    VERSION += "-prod"
    MEDIA_URL = 'http://supcik.github.com/www.brahier.ch/static/'
else:
    DEBUG = True
    VERSION += "-dev"
    MEDIA_URL = '/static/'

TEMPLATE_DEBUG = DEBUG
