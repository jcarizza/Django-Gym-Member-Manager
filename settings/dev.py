"""
Django settings for Gymnasium project in dev mode.
"""

from .base import *

DEBUG=True
SECRET_KEY = 'too-secret'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS += [
    'django_extensions'
]

LANGUAGE_CODE = 'es-AR'
TIME_ZONE = 'America/Argentina/Buenos_Aires'