"""
Manager for the User model.
"""

# Import system modules
import logging

# Import Django modules
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """
    The Manager for a User.
    """

    def create_user(self, username, email, password=None):
        """
        Create a new user with the given username, password, and email.

        :param username: the username for the new user
        :param email: the email for the new user
        :param password: the password for the new user
        :return: the created object
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create a new super upser with admin privileges.

        :param username: the username for the new user
        :param email: the email for the new user
        :param password: the password for the new user
        :return: the created object
        """
        user = self.create_user(username=username,
                                email=email,
                                password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
