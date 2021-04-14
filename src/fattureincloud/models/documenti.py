"""Anagrafica app."""
from datetime import date

from fattureincloud.models.base import Resource


class Documenti(Resource):
    """Documenti class."""

    list_key = "lista_documenti"

    def lista(
        self,
        anno_competenza=None,
        data_inizio="",
        data_fine="",
        cliente="",
        id_cliente="",
        saldato="",
        oggetto="",
        pagina=1,
    ):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "anno_competenza": anno_competenza or date.today().year,
            "data_inizio": data_inizio
            or date(year=date.today().year, month=1, day=1).strftime("%d/%m/%Y"),
            "data_fine": data_fine
            or date(year=date.today().year, month=12, day=31).strftime("%d/%m/%Y"),
            "cliente": cliente,
            "id_cliente": id_cliente,
            "saldato": saldato,
            "oggetto": oggetto,
            "pagina": pagina,
        }
        return super().lista(**payload)

    def dettagli(self, _id="", token=""):
        """Return document's details."""
        payload = {"id": _id, "token": token}
        return self.requester.post(f"{self.path}dettagli", payload).get(
            "dettagli_documento", {}
        )

    def nuovo(self, **kwargs):
        """Create new document."""
        raise NotImplementedError

    def modifica(self, **kwargs):
        """Update document."""
        raise NotImplementedError

    def elimina(self, **kwargs):
        """Delete document."""
        raise NotImplementedError

    def info(self, anno_competenza=None):
        """Return useful information to create document."""
        payload = {"anno_competenza": anno_competenza or date.today().year}
        return self.requester.post(f"{self.path}info", payload).get("info", {})

    def infomail(self, _id="", token=""):
        """Return document's info mail."""
        payload = {"id": _id, "token": token}
        return self.requester.post(f"{self.path}infomail", payload)

    def inviamail(self, **kwargs):
        """Send document through email."""
        raise NotImplementedError


class Fatture(Documenti):
    """Fatture class."""

    pass


class Proforma(Documenti):
    """Proforma class."""

    pass


class Ordini(Documenti):
    """Ordini class."""

    pass


class Preventivi(Documenti):
    """Preventivi class."""

    pass


class NDC(Documenti):
    """NDC class."""

    pass


class Ricevute(Documenti):
    """Ricevute class."""

    pass


class DDT(Documenti):
    """DDT class."""

    pass
