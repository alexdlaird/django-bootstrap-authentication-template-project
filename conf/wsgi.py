"""
WSGI configuration for Django environment.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

application = get_wsgi_application()

# Only start the monitor if we're using a non-dev web server and not in production
if not settings.DEV_SERVER:
    from conf import monitor

    monitor.start()
