"""Client definition."""
import requests

from .exceptions import FattureInCloudExcpetion
from .models.acquisti import Acquisti
from .models.anagrafica import Clienti, Fornitori
from .models.corrispettivi import Corrispettivi
from .models.documenti import DDT, NDC, Fatture, Ordini, Preventivi, Proforma, Ricevute
from .models.magazzino import ArriviMerce
from .models.mail import Mail
from .models.prodotti import Prodotti


class FattureInCloudAPI:
    """
    FattureInCloudAPI class.

    :param api_uid: the api_uid you may provide
    :param api_key: the api_key you may provide
    """

    def __init__(self, api_uid, api_key):
        """Create a client instance."""
        self.api_uid = api_uid
        self.api_key = api_key
        self.host = "https://api.fattureincloud.it/v1"
        self.request_maker = RequestMaker(api_uid, api_key, self.host)

        #  Anagrafica
        self.clienti = Clienti(self.request_maker)
        self.fornitori = Fornitori(self.request_maker)

        # Prodotti
        self.prodotti = Prodotti(self.request_maker)

        # Documenti
        self.fatture = Fatture(self.request_maker)
        self.proforma = Proforma(self.request_maker)
        self.ordini = Ordini(self.request_maker)
        self.preventivi = Preventivi(self.request_maker)
        self.ndc = NDC(self.request_maker)
        self.ricevute = Ricevute(self.request_maker)
        self.ddt = DDT(self.request_maker)

        # Acquisti
        self.acquisti = Acquisti(self.request_maker)

        # Corrispettivi
        self.corrispettivi = Corrispettivi(self.request_maker)

        # Magazzino
        self.arrivimerce = ArriviMerce(self.request_maker)

        # Mail
        self.mail = Mail(self.request_maker)

    def info(self):
        """Return info."""
        return self.request_maker.post("/richiesta/info")

    def account(self):
        """Return account info."""
        return self.request_maker.post("/info/account")


class RequestMaker:
    """
    RequestMaker class.

    :param api_uid: the api_uid you may provide
    :param api_key: the api_key you may provide
    """

    def __init__(self, api_uid, api_key, host):
        """Create a client instance."""
        self.api_uid = api_uid
        self.api_key = api_key
        self.host = host

    def post(self, path, data=None):
        if data is None:
            data = {}
        data["api_uid"] = self.api_uid
        data["api_key"] = self.api_key

        result = requests.post(f"{self.host}{path}", json=data)
        error_message = result.content
        if 200 <= result.status_code < 300:
            json_response = result.json()
            if "error" in json_response:
                error_message = json_response["error"]
            else:
                return json_response

        raise FattureInCloudExcpetion(
            message=error_message,
            status_code=result.status_code,
            body=result.content,
        )
