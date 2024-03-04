"""
Base URL configuration.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import sys

from django.conf import settings as config
from django.urls import include, re_path
from django.views import static

import myproject.auth.urls
import myproject.common.urls
import myproject.myapp.urls

urlpatterns = [
    # Include app-specific URL files
    re_path(r'^', include(myproject.common.urls)),
    re_path(r'^', include(myproject.auth.urls)),
    re_path(r'^', include(myproject.myapp.urls)),
]

if config.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if config.DEBUG or 'test' in sys.argv:
    # Ensure media files are shown properly when using a dev server
    urlpatterns += [
        re_path(r'^' + config.MEDIA_URL.lstrip('/') + '(?P<path>.*)$', static.serve, {
            'document_root': config.MEDIA_ROOT})
    ]
