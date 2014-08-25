"""
User model.
"""

# Import system modules
import logging

# Import Django modules
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core import validators

# Import project modules
from ..managers.usermanager import UserManager

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class User(AbstractBaseUser):
    """
    The model for a User.
    """

    # Basic user and authentication fields
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                                              _('Enter a valid username. '
                                                                'This value may contain only letters, numbers '
                                                                'and @/./+/-/_ characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Personal info fields
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    
    # Set the manager
    users = UserManager()

    # Fields required to define the abstracted Django user
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __unicode__(self):
        """
        Return the unicode representation of the class.
        
        :return: unicode representation of the class
        """
        return unicode(self.pk)

    def get_full_name(self):
        """
        Retreieve the long name for the user.

        :return: The user's email address.
        """
        return self.email

    def get_short_name(self):
        """
        Retreieve the short name for the user.

        :return: The user's email address.
        """
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if this user has the given permission.

        :return: True if the user has the permission, False otherwise.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Check if the user has privileges to the given app

        :return: True if the user has privileges for app, False otherwise
        """
        return True

    @property
    def is_staff(self):
        """
        Check if this user has administrative privileges.

        :return: True if the user has admin, False otherwise
        """
        return self.is_admin

    @property
    def is_superuser(self):
        """
        Check if the user has administrative privileges.

        :return: True if the user has admin, False otherwise
        """
        return self.is_admin
