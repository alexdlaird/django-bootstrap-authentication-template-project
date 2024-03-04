"""
Publicly accessible named URLs should be defined here to ensure they are properly listed in the generated /sitemap.xml.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'login', 'forgot', 'register']

    def location(self, obj):
        return reverse(obj)
