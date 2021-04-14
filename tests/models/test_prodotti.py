from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestProdotti(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_prodotti(self, mocker):
        """Test prodotti."""
        mocker_register_uri(
            mocker, self.client.host, "/prodotti/lista", "prodotti/prodotti.json"
        )
        self.assertEqual(len(self.client.prodotti.lista()), 2)

    @Mocker()
    def test_prodotti_2_pages(self, mocker):
        """Test prodotti with 2 pages."""
        mocker_register_uri(
            mocker,
            self.client.host,
            "/prodotti/lista",
            "prodotti/prodotti_2_pages.json",
        )
        self.assertEqual(len(self.client.prodotti.lista()), 4)

    def test_nuovo(self):
        """Test nuovo method."""

        with self.assertRaises(NotImplementedError):
            self.client.prodotti.nuovo()

    def test_importa(self):
        """Test importa method."""

        with self.assertRaises(NotImplementedError):
            self.client.prodotti.importa()

    def test_modifica(self):
        """Test modifica method."""

        with self.assertRaises(NotImplementedError):
            self.client.prodotti.modifica()

    def test_elimina(self):
        """Test elimina method."""

        with self.assertRaises(NotImplementedError):
            self.client.prodotti.elimina()
