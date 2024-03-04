"""
Unauthenticated general view entrance functions.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import logging

from django.http import HttpResponseRedirect
from django.urls import reverse

logger = logging.getLogger(__name__)


def home(request):
    redirect = reverse('login')
    if request.user.is_authenticated:
        redirect = reverse('portal')

    return HttpResponseRedirect(redirect)
