"""Client definition."""
import requests

from .exceptions import FattureInCloudExcpetion
from .models.anagrafica import Clienti, Fornitori


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

        self.clienti = Clienti(self.request_maker)
        self.fornitori = Fornitori(self.request_maker)

    def info(self):
        """Return info."""
        return self.request_maker.post("/richiesta/info")


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
