from requests_mock import Mocker

from tests.mocking import mocker_register_uri
from tests.test_client import TestClient


class TestProdotti(TestClient):
    """Define simple test case for base client request."""

    @Mocker()
    def test_prodotti(self, mocker):
        """Test prodotti."""
        mocker_register_uri(
            mocker, self.client.host, "/prodotti/lista", "prodotti/prodotti.json"
        )
        self.assertEqual(len(self.client.prodotti.lista()), 2)
