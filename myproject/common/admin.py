__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.conf import settings
from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite


class MyProjectAdminSite(AdminSite):
    """
    Creates a base AdminSite for this project. Models and URLs should be attached to an instance of this class.
    """
    site_header = settings.PROJECT_NAME + ' Administration'
    site_title = site_header
    index_title = settings.PROJECT_NAME


class BaseModelAdmin(ModelAdmin):
    """
    All Models that inherit from BaseModel should also inherit from this BaseModelAdmin, which makes sure the common
    attributes are properly rendered in the admin area.
    """
    list_display = ('created_at', 'updated_at',)
    ordering = ('-updated_at',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('created_at', 'updated_at',)

        return self.readonly_fields


# Instantiate the Admin site
admin_site = MyProjectAdminSite()
