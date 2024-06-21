__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import os
import sys
from urllib.parse import urlparse

from django.apps import AppConfig
from django.conf import settings


class CommonConfig(AppConfig):
    name = 'myproject.common'
    verbose_name = 'Common'

    PROJECT_HOST = settings.PROJECT_HOST

    def ready(self):
        if settings.USE_NGROK and os.environ.get("NGROK_AUTHTOKEN"):
            # pyngrok will only be installed, and should only ever be initialized, in a dev environment
            from pyngrok import ngrok

            # Get the dev server port (defaults to 8000 for Django, can be overridden with the
            # last arg when calling `runserver`)
            addrport = urlparse(f"http://{sys.argv[-1]}")
            port = addrport.port if addrport.netloc and addrport.port else 8000

            # Open a ngrok tunnel to the dev server
            public_url = ngrok.connect(port)
            print(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

            # Update any base URLs or webhooks to use the public ngrok URL
            self.PROJECT_HOST = public_url
            CommonConfig.init_webhooks(public_url)

    @staticmethod
    def init_webhooks(callback_url):
        pass
