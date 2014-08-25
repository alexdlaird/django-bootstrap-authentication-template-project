"""
Define the Admin site.
"""

# Import Django modules
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

# Import project modules
from myapp.models import User
from forms import UserChangeForm, UserCreationForm

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'


class MyAppUserAdmin(UserAdmin):
    """
    Definition for a user in the Admin area.
    """
    # The forms to add and change user details
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the table of users
    list_display = ('username', 'email', 'is_admin')
    # Items that are filterable on the admin page
    list_filter = ('is_admin',)
    # Fieldsets displayed in the admin, order matters
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'last_login')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
        ('Personal Info', {'fields': (
            'first_name',
            'last_name'
        )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    # Fields on which the admin can search
    search_fields = ('username', 'email',)
    # Ordering of fields
    ordering = ('username', 'email',)
    filter_horizontal = ()


class MyProjectAdminSite(AdminSite):
    """
    Definition for the Admin site.
    """
    site_header = settings.PROJECT_NAME + ' Administration'
    site_title = site_header
    index_title = settings.PROJECT_NAME

# Instantiate the Admin site
myproject_admin_site = MyProjectAdminSite()

# Register the models in the Admin
myproject_admin_site.register(User, MyAppUserAdmin)