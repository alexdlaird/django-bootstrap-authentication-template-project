"""
Context processors for project-specific attributes to be passed to templates.
"""

# Import Django modules
from django.conf import settings

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineer'
__version__ = '0.0.1'


def template(request):
    """
    Append project-specific attributes to a request context.

    :param request: the page request
    :return: a dictionary of context elements
    """
    context = {
        'PROJECT_NAME': settings.PROJECT_NAME,
        'PROJECT_VERSION': settings.PROJECT_VERSION
    }
    return context