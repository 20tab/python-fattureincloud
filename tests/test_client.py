from unittest import TestCase
from unittest.mock import patch

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from fattureincloud.exceptions import FattureInCloudExcpetion
from tests.mocking import MockedErrorResponse, mocker_register_uri


class TestClient(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    def test_client_init(self):
        """Test client initialization."""
        self.assertIsInstance(self.client, FattureInCloudAPI)

    @Mocker()
    def test_post(self, mocker):
        """Test requester post method."""

        mocker_register_uri(mocker, self.client.host, "/richiesta/info", "info.json")
        EXPECTED = {
            "messaggio": "I parametri 'api_key' e 'api_uid' sono corretti.",
            "limite_breve": "Rimangono 29 richieste per i prossimi 60 secondi",
            "limite_medio": "Rimangono 499 richieste per i prossimi 3600 secondi",
            "limite_lungo": "Rimangono 36929 richieste per i prossimi 1142233 secondi",
            "success": True,
        }
        res = self.client.info()
        self.assertEqual(res, EXPECTED)

    @Mocker()
    def test_post_error(self, mocker):
        """Test requester post method with error."""

        mocker_register_uri(mocker, self.client.host, "/richiesta/info", "error.json")
        with self.assertRaises(FattureInCloudExcpetion):
            self.client.info()

    @patch("requests.post", return_value=MockedErrorResponse())
    def test_post_error_status_code(self, m):
        """Test requester post method with error status code."""

        with self.assertRaises(FattureInCloudExcpetion):
            self.client.info()
