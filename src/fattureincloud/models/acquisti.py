"""Anagrafica app."""
from datetime import date

from fattureincloud.models.base import Resource


class Acquisti(Resource):
    """Acquisti class."""

    list_key = "lista_documenti"

    def lista(
        self,
        anno="",
        tipo="",
        data_inizio="",
        data_fine="",
        fornitore="",
        id_fornitore="",
        saldato="",
        mostra_link_allegato="",
    ):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "anno": anno or date.today().year,
            "tipo": tipo,
            "data_inizio": data_inizio
            or date(year=date.today().year, month=1, day=1).strftime("%d/%m/%Y"),
            "data_fine": data_fine
            or date(year=date.today().year, month=12, day=31).strftime("%d/%m/%Y"),
            "fornitore": fornitore,
            "id_fornitore": id_fornitore,
            "saldato": saldato,
            "mostra_link_allegato": mostra_link_allegato,
        }
        return super().lista(**payload)

    def dettagli(self, _id=""):
        """Return acquisti's details."""
        payload = {"id": _id}
        return self.requester.post(f"{self.path}dettagli", payload).get(
            "dettagli_documento", {}
        )

    def nuovo(self, **kwargs):
        """Create new acquisti."""
        raise NotImplementedError

    def importa(self, **kwargs):
        """Import a list of acquisti."""
        raise NotImplementedError

    def modifica(self, **kwargs):
        """Update acquisti."""
        raise NotImplementedError

    def elimina(self, **kwargs):
        """Delete acquisti."""
        raise NotImplementedError
