from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestMail(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_mail(self, mocker):
        """Test mail."""
        mocker_register_uri(
            mocker, self.client.host, "/mail/lista", "mail/mail.json"
        )
        self.assertEqual(len(self.client.mail.lista()), 1)

