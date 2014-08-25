"""
Base URLs.
"""

# Import Django modules
from django.conf.urls import patterns, include, url
from django.contrib import admin

# Import project modules
from myproject.admin import myproject_admin_site
from myapp.views import *

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

urlpatterns = [
    # Admin URLs
    url(r'^admin/', include(myproject_admin_site.urls), name='admin'),

    # Base URL
    url(r'^$', home, name='home'),
    
    # Authentication URLs
    url(r'^login$', login, name='login'),
    url(r'^logout', logout, name='logout'),
    url(r'^forgot$', forgot, name='forgot'),
    
    # Authenticated URLs
    url(r'^myapp$', myapp, name='myapp'),
    url(r'^settings$', settings, name='settings'),
]
