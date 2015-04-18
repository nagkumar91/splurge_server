from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'splurge_server',
        'USER': 'nagkumar',
        'PASSWORD': 'root123',
        'HOST': '',
        'PORT': '',
    }
}