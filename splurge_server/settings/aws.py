__author__ = 'nagkumar'
from .base import *
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