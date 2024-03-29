__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def send_multipart_email(template_name, context, subject, to, bcc=None):
    """
    Send a multipart text/html email.

    :param template_name: The path to the template (no extension), assuming both a .txt and .html version are present
    :param context: A dictionary of context elements to pass to the email templates
    :param subject: The subject of the email
    :param to: A list of email addresses to which to send
    :param bcc: A list of email addresses to which to BCC
    :return:
    """
    plaintext = get_template(f'{template_name}.txt')
    html = get_template(f'{template_name}.html')
    text_content = plaintext.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, to, bcc)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
