"""
Settings specific to prod-like deployable code, reading values from system environment variables.
"""

import os

from conf.settings import PROJECT_ID
from .common import DEFAULT_TEMPLATES, DEFAULT_MIDDLEWARE, DEFAULT_INSTALLED_APPS, DEBUG, PROJECT_NAME, \
    ADMIN_EMAIL_ADDRESS

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Alex Laird'
__version__ = '0.2.0'

# Application definition

INSTALLED_APPS = DEFAULT_INSTALLED_APPS

MIDDLEWARE = DEFAULT_MIDDLEWARE

TEMPLATES = DEFAULT_TEMPLATES

if DEBUG:
    TEMPLATES[0]['OPTIONS']['context_processors'] += (
        'django.template.context_processors.debug',
    )

#############################
# Django configuration
#############################

# Security

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Logging

if not DEBUG:
    ADMINS = (
        (PROJECT_NAME, ADMIN_EMAIL_ADDRESS),
    )
    MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'django_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/{}/django.log'.format(PROJECT_ID),
            'maxBytes': 50000000,
            'backupCount': 3,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        '{}_common_log'.format(PROJECT_ID): {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/{}/common.log'.format(PROJECT_ID),
            'maxBytes': 50000000,
            'backupCount': 3,
            'formatter': 'standard',
        },
        '{}_auth_log'.format(PROJECT_ID): {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/{}/auth.log'.format(PROJECT_ID),
            'maxBytes': 50000000,
            'backupCount': 3,
            'formatter': 'standard',
        },
        '{}_myapp_log'.format(PROJECT_ID): {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/{}/myapp.log'.format(PROJECT_ID),
            'maxBytes': 50000000,
            'backupCount': 3,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_log', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.common'.format(PROJECT_ID): {
            'handlers': ['{}_common_log'.format(PROJECT_ID), 'mail_admins'],
            'level': 'INFO',
        },
        'myproject.auth'.format(PROJECT_ID): {
            'handlers': ['{}_auth_log'.format(PROJECT_ID), 'mail_admins'],
            'level': 'INFO',
        },
        'myproject.myapp'.format(PROJECT_ID): {
            'handlers': ['{}_myapp_log'.format(PROJECT_ID), 'mail_admins'],
            'level': 'INFO',
        },
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('MYPROJECT_REDIS_HOST'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}

# Database

DATABASES = {
    'default': {
        'NAME': os.environ.get('MYPROJECT_DB_NAME'),
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('MYPROJECT_DB_HOST'),
        'USER': os.environ.get('MYPROJECT_DB_USER'),
        'PASSWORD': os.environ.get('MYPROJECT_DB_PASSWORD'),
    }
}
