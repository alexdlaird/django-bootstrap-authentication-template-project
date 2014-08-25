"""
View entrance functions.
"""

# Import system modules
import logging
import pytz

# Import Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

# Import project modules
from auth import process_login, process_logout, process_forgot_password

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


def home(request):
    redirect = reverse('login')
    if request.user.is_authenticated():
        redirect = reverse('myapp')

    return HttpResponseRedirect(redirect)


def login(request):
    redirect = None
    if request.user.is_authenticated():
        redirect = reverse('myapp')
    else:
        if request.method == 'POST':
            redirect = process_login(request)

        status_div = request.session.get('status_div', '')
        if status_div == '':
            status_div = request.COOKIES.get('status_div', '')
        if 'status_div' in request.session:
            del request.session['status_div']

    if redirect:
        redirect = HttpResponseRedirect(redirect)
        return redirect
    else:
        response = render(request, 'login.html', {'status_div': status_div})
        if 'status_div' in request.COOKIES:
            response.delete_cookie(key='status_div')
        return response


def logout(request):
    process_logout(request)

    return HttpResponseRedirect(reverse('home'))


def forgot(request):
    redirect = None
    status_div = ''
    if request.user.is_authenticated():
        redirect = reverse('settings')
    else:
        if request.method == 'POST':
            redirect = process_forgot_password(request)

        status_div = request.session.get('status_div', '')
        if 'status_div' in request.session:
            del request.session['status_div']

    if not redirect:
        return render(request, 'forgot.html', {'status_div': status_div})
    else:
        response = HttpResponseRedirect(redirect)
        if 'status_div' != '':
            response.set_cookie('status_div', status_div)
        return response


@login_required
def myapp(request):
    timezone.activate(pytz.timezone(request.user.time_zone))
    
    return render(request, "myapp.html")


@login_required
def settings(request):
    timezone.activate(pytz.timezone(request.user.time_zone))

    return render(request, "settings.html")