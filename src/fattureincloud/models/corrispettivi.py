"""Anagrafica app."""
from datetime import date

from fattureincloud.models.base import Resource


class Corrispettivi(Resource):
    """Corrispettivi class."""

    list_key = "lista_corrispettivi"

    def lista(self, anno="", tipo="", data_inizio="", data_fine="", _id=""):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "anno": anno or date.today().year,
            "tipo": tipo,
            "data_inizio": data_inizio
            or date(year=date.today().year, month=1, day=1).strftime("%d/%m/%Y"),
            "data_fine": data_fine
            or date(year=date.today().year, month=12, day=31).strftime("%d/%m/%Y"),
            "id": _id,
        }
        return super().lista(**payload)

    def nuovo(self, **kwargs):
        """Create new corrispettivi."""
        raise NotImplementedError

    def modifica(self, **kwargs):
        """Update corrispettivi."""
        raise NotImplementedError

    def elimina(self, **kwargs):
        """Delete corrispettivi."""
        raise NotImplementedError
