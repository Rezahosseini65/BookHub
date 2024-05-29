from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
]+INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookhub',
        'USER': 'bookhub',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}
