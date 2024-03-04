"""
Authenticated app URLs.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.urls import re_path

from myproject.myapp.views import portal

urlpatterns = [
    # Authenticated URLs
    re_path(r'^portal', portal, name='portal'),
]
