"""
Authentication functions.
"""

# Import system modules
import logging

# Import Django modules
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


def process_login(request):
    redirect = None
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        error_msg = None
        if user is not None:
            if user.is_active:
                login(request, user)
                logger.info('Logged in user ' + username)
                redirect = reverse('myapp')

                if request.POST.get('remember-me', False):
                    request.session.set_expiry(1209600)

                # If 'next' exists as a parameter in the URL, redirect to the specified page instead
                if 'next' in request.GET:
                    redirect = request.GET['next']
            else:
                logger.info('Inactive user ' + username + " attempted login")
                error_msg = 'Sorry, your account has been disabled. <a href="mailto:project@host.com">Get in touch with us</a> and we\'ll help you sort this out!'
        else:
            logger.info('Non-existent user ' + username + " attempted login")
            error_msg = 'Oops! We don\'t recognize that account. Check to make sure you entered your credentials properly.'

        if error_msg != None:
            request.session['status_div'] = '<div id="login-status" class="alert alert-warning">' + error_msg + '</div>'

    return redirect


def process_logout(request):
    username = request.user.username
    logout(request)
    logger.info('Logged out user ' + username)


def process_forgot_password(request):
    email = request.POST['email']
    redirect = None
    try:
        user = get_user_model().users.get(email=email)

        # Generate a random password and save it to the user
        password = get_user_model().users.make_random_password()
        user.set_password(password)
        user.save()
        logger.info('Reset password for user with email ' + email)

        # Generate the email and send the password to the user
        plaintext = get_template('email_forgot.txt')
        html = get_template('email_forgot.html')
        c = Context({'first_name': user.first_name, 'password': password,
                     'site_url': ('https://' if request.is_secure() else 'http://') + request.get_host()})
        text_content = plaintext.render(c)
        html_content = html.render(c)

        msg = EmailMultiAlternatives('Your My Project Password Has Been Reset', text_content,
                                     settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        request.session[
            'status_div'] = '<div id="login-status" class="alert alert-info">Alright, we\'ve sent sent a temporary password to that email address. Login to your account and change your password it immediately.</div>'
        request.session.modified = True

        redirect = reverse('login')
    except get_user_model().DoesNotExist:
        logger.info('A visitor tried to reset the password for an unknown email address of ' + email)
        request.session[
            'status_div'] = '<div id="login-status" class="alert alert-warning">Sorry, that email doesn\'t belong to any user in our system. Talk to HR and they can get you added into the system.</div>'

    return redirect