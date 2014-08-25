"""
Settings for a development environment.
"""

# Import system modules
import os
import warnings

# Import project modules
from .common import DEFAULT_TEMPLATE_CONTEXT_PROCESSORS, DEFAULT_MIDDLEWARE_CLASSES, DEFAULT_INSTALLED_APPS

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'


# Define the base working directory of the application
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Application definition

INSTALLED_APPS = DEFAULT_INSTALLED_APPS + (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.debug',
)


#############################
# Django configuration
#############################

# Security

SECRET_KEY = 'ui(0mu1=%8pfnnuy0i&8dlf*whlfo4_u6&4mlm)c90aoj1_etn'
CSRF_MIDDLEWARE_SECRET = '7A0+@mDw*5hA=Bzh${L%r;7Hbcut|.7_#)BJcZi{)IGN?Z^1Ya'
ALLOWED_HOSTS = ['localhost']
INTERNAL_IPS = (
    '127.0.0.1',
)

# Logging

DEBUG = True
TEMPLATE_DEBUG = True

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
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'myproject_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'myproject_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'myapp_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'myapp_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject': {
            'handlers': ['console', 'myproject_log'],
            'level': 'DEBUG',
        },
        'myapp': {
            'handlers': ['console', 'myapp_log'],
            'level': 'DEBUG',
        },
    }
}

# When in development, we want to be warned about dates that don't have a timezone
warnings.filterwarnings('error', r"DateTimeField .* received a naive datetime", RuntimeWarning,
                        r'django\.db\.models\.fields')

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}