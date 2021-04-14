"""Anagrafica app."""
from datetime import date

from fattureincloud.models.base import Resource


class ArriviMerce(Resource):
    """ArriviMerce class."""

    list_key = "lista_documenti"

    def lista(
        self,
        anno="",
        data_inizio="",
        data_fine="",
        fornitore="",
        id_fornitore="",
        mostra_link_allegato="",
    ):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "anno": anno or date.today().year,
            "data_inizio": data_inizio
            or date(year=date.today().year, month=1, day=1).strftime("%d/%m/%Y"),
            "data_fine": data_fine
            or date(year=date.today().year, month=12, day=31).strftime("%d/%m/%Y"),
            "fornitore": fornitore,
            "id_fornitore": id_fornitore,
            "mostra_link_allegato": mostra_link_allegato,
        }
        return super().lista(**payload)

    def dettagli(self, _id=""):
        """Return arrivimerce's details."""
        payload = {"id": _id}
        return self.requester.post(f"{self.path}dettagli", payload).get(
            "dettagli_documento", {}
        )
