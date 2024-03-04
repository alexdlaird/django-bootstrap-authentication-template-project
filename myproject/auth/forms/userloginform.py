__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django import forms

from myproject.common.forms.baseform import BaseForm


class UserLoginForm(forms.Form, BaseForm):
    username = forms.CharField(label='Username')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
