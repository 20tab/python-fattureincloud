from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestAnagrafica(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_clienti(self, mocker):
        """Test clienti."""
        mocker_register_uri(
            mocker, self.client.host, "/clienti/lista", "anagrafica/clienti.json"
        )
        self.assertEqual(len(self.client.clienti.lista()), 4)

    @Mocker()
    def test_fornitori(self, mocker):
        """Test fornitori."""
        mocker_register_uri(
            mocker, self.client.host, "/fornitori/lista", "anagrafica/fornitori.json"
        )
        self.assertEqual(len(self.client.fornitori.lista()), 2)

    def test_nuovo(self):
        """Test nuovo method."""

        with self.assertRaises(NotImplementedError):
            self.client.clienti.nuovo()

    def test_importa(self):
        """Test importa method."""

        with self.assertRaises(NotImplementedError):
            self.client.clienti.importa()

    def test_modifica(self):
        """Test modifica method."""

        with self.assertRaises(NotImplementedError):
            self.client.clienti.modifica()

    def test_elimina(self):
        """Test elimina method."""

        with self.assertRaises(NotImplementedError):
            self.client.clienti.elimina()
