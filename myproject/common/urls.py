__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.conf import settings as config
from django.urls import re_path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView, TemplateView

from myproject.common.admin import admin_site
from myproject.common.sitemaps import StaticViewSitemap
from myproject.common.views import home

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Top-level URLs
    re_path(r'^admin/', admin_site.urls),

    # Crawler shortcuts and placeholders
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain; charset=utf-8')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=config.STATIC_URL + 'favicon.ico', permanent=True)),
    re_path(r'^favicon\.png$', RedirectView.as_view(url=config.STATIC_URL + 'favicon.png', permanent=True)),

    # General URLs
    re_path(r'^$', home, name='home'),
]
