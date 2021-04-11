from requests_mock import Mocker

from tests.mocking import mocker_register_uri
from tests.test_client import TestClient


class TestAnagrafica(TestClient):
    """Define simple test case for base client request."""

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
