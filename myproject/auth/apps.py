__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'myproject.auth'
    label = 'myproject_auth'
    verbose_name = 'Authentication'
