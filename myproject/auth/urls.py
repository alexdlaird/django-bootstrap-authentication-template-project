"""
Authentication URLs.
"""

from django.urls import re_path

from myproject.auth.views import login, logout, forgot, settings, register

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Alex Laird"
__version__ = "0.6.0"

urlpatterns = [
    # Authentication URLs
    re_path(r'^register$', register, name='register'),
    re_path(r'^login$', login, name='login'),
    re_path(r'^logout', logout, name='logout'),
    re_path(r'^forgot$', forgot, name='forgot'),

    # Account URLs
    re_path(r'^settings$', settings, name='settings'),
]
