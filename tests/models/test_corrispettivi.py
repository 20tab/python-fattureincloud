from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestCorrispettivi(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_corrispettivi(self, mocker):
        """Test corrispettivi."""
        mocker_register_uri(
            mocker,
            self.client.host,
            "/corrispettivi/lista",
            "corrispettivi/corrispettivi.json",
        )
        self.assertEqual(len(self.client.corrispettivi.lista()), 1)

    def test_nuovo(self):
        """Test nuovo method."""

        with self.assertRaises(NotImplementedError):
            self.client.corrispettivi.nuovo()

    def test_modifica(self):
        """Test modifica method."""

        with self.assertRaises(NotImplementedError):
            self.client.corrispettivi.modifica()

    def test_elimina(self):
        """Test elimina method."""

        with self.assertRaises(NotImplementedError):
            self.client.corrispettivi.elimina()
