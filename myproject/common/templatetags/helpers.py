__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    """
    Returns 'active' if the give pattern is in the current URL.
    """
    try:
        if (request.path == '/' == pattern) or (pattern != '/' and request.path.startswith(pattern)):
            return 'active'
    except:  # pragma: no cover
        pass
    return ''
