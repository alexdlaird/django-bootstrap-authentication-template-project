"""
Context processors for project-specific attributes to be passed to all templates.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.conf import settings


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
