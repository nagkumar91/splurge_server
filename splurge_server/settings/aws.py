__author__ = 'nagkumar'
from .base import *

DEBUG = True
# ALLOWED_HOSTS = ['getsplurge.com', 'splurge.nagkumar.com', '']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

STATIC_URL = '/static/'

MEDIA_ROOT = "/var/www/splurge/media"

MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'splurge',
        'USER': 'splurge',
        'PASSWORD': 'splurg3',
        'HOST': '',
        'PORT': '',
    }
}