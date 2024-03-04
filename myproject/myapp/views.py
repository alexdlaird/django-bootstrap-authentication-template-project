"""
Authenticated view entrance functions.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import logging

import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

logger = logging.getLogger(__name__)


@login_required
def portal(request):
    timezone.activate(pytz.timezone(request.user.time_zone))

    return render(request, "portal.html")
