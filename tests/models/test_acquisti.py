from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestAcquisti(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_acquisti(self, mocker):
        """Test acquisti."""
        mocker_register_uri(
            mocker, self.client.host, "/acquisti/lista", "acquisti/acquisti.json"
        )
        self.assertEqual(len(self.client.acquisti.lista()), 2)

    @Mocker()
    def test_acquisti_dettagli(self, mocker):
        """Test acquisti dettagli."""
        mocker_register_uri(
            mocker, self.client.host, "/acquisti/dettagli", "acquisti/dettagli.json"
        )
        details = self.client.acquisti.dettagli(_id=12)
        self.assertEqual(details.get("id"), "12")

    def test_nuovo(self):
        """Test nuovo method."""

        with self.assertRaises(NotImplementedError):
            self.client.acquisti.nuovo()

    def test_modifica(self):
        """Test modifica method."""

        with self.assertRaises(NotImplementedError):
            self.client.acquisti.modifica()

    def test_elimina(self):
        """Test elimina method."""

        with self.assertRaises(NotImplementedError):
            self.client.acquisti.elimina()
