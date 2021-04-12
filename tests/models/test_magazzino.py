from unittest import TestCase

from requests_mock import Mocker

from fattureincloud.client import FattureInCloudAPI
from tests.mocking import mocker_register_uri


class TestArriviMerce(TestCase):
    """Define simple test case for base client request."""

    maxDiff = None

    def setUp(self):
        """Set client with key and uid."""
        self.client = FattureInCloudAPI(api_uid="123456", api_key="qwerty")

    @Mocker()
    def test_arrivimerce(self, mocker):
        """Test arrivimerce."""
        mocker_register_uri(
            mocker, self.client.host, "/arrivimerce/lista", "magazzino/arrivimerce.json"
        )
        self.assertEqual(len(self.client.arrivimerce.lista()), 1)

    @Mocker()
    def test_arrivimerce_dettagli(self, mocker):
        """Test arrivimerce dettagli."""
        mocker_register_uri(
            mocker, self.client.host, "/arrivimerce/dettagli", "magazzino/dettagli.json"
        )
        details = self.client.arrivimerce.dettagli(_id=13)
        self.assertEqual(details.get("id"), "13")
