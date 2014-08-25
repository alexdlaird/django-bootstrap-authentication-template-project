"""
Streamlined Django settings for running test cases.
"""

# Import system modules
import os
import sys
import logging

# Import project modules
from .common import DEFAULT_TEMPLATE_CONTEXT_PROCESSORS, DEFAULT_MIDDLEWARE_CLASSES, DEFAULT_INSTALLED_APPS

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'


# Define the base working directory of the application
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))


# Application definition

INSTALLED_APPS = DEFAULT_INSTALLED_APPS

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS

# This is an insecure password hasher, but much faster than what would be used in production
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


# Security configuration

SECRET_KEY = 'vb*dxh%m4-!g^=fiozd4t@38j2voupkom-%*8&t%5p+lkfk5em'

ALLOWED_HOSTS = ['localhost']


# Logging configuration

# DO_LOGGING is false by default to improve efficiency and speed of tests, but it can be set to true to enable logging
# when writing or debugging tests
TEST_DEBUG = False

if TEST_DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'django_log': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'django_test_log'),
                'formatter': 'standard',
            },
            'myproject_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'myproject_test_log'),
                'formatter': 'standard',
            },
            'myapp_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'myapp_test_log'),
                'formatter': 'standard',
            },
            'console': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['django_log', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'myproject': {
                'handlers': ['myproject_log'],
                'level': 'DEBUG',
            },
            'myapp': {
                'handlers': ['maypp_log'],
                'level': 'DEBUG',
            },
        }
    }
else:
    logging.disable(logging.ERROR)


# Database configuration

# STAGING_DATABASE is false by default to improve efficiency and speed of tests, but it can be set to true to ensure all tests
# still pass when using the staging server's database
STAGING_DATABASE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.test.sqlite3'),
    }
}
if STAGING_DATABASE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': 'db_host',
            'NAME': 'myproject',
            'USER': 'db_user',
            'PASSWORD': 'db_password',
        }
    }