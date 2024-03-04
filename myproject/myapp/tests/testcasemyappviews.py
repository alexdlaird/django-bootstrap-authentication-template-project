__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django.test import TestCase
from django.urls import reverse

from myproject.auth.tests.helpers import userhelper


class TestCaseMyAppViews(TestCase):
    def test_portal_view(self):
        # GIVEN
        userhelper.given_a_user_exists_and_is_logged_in(self.client)

        # WHEN
        response = self.client.get(reverse('portal'))

        # THEN
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portal.html')
