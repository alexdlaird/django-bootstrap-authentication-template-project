"""
Authentication URLs.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.urls import re_path

from myproject.auth.views import login, logout, forgot, settings, register

urlpatterns = [
    # Authentication URLs
    re_path(r'^register$', register, name='register'),
    re_path(r'^login$', login, name='login'),
    re_path(r'^logout', logout, name='logout'),
    re_path(r'^forgot$', forgot, name='forgot'),

    # Account URLs
    re_path(r'^settings$', settings, name='settings'),
]
