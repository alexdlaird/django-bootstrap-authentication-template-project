"""
Publicly accessible named URLs should be defined here to ensure they are properly listed in the generated /sitemap.xml.
"""

from django.contrib import sitemaps
from django.core.urlresolvers import reverse

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Alex Laird'
__version__ = '0.2.0'


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'login', 'forgot', 'register']

    def location(self, item):
        return reverse(item)
