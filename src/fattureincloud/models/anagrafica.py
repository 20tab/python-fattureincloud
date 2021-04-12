"""Anagrafica app."""
from fattureincloud.models.base import Resource


class Soggetto(Resource):
    """Soggetto class."""

    def lista(self, _id="", filtro="", nome="", cf="", piva="", pagina=1):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "id": _id,
            "filtro": filtro,
            "nome": nome,
            "cf": cf,
            "piva": piva,
            "pagina": pagina,
        }
        return super().lista(**payload)

    def nuovo(self, **kwargs):
        """Create new soggetto."""
        raise NotImplementedError

    def importa(self, **kwargs):
        """Import a list of soggetto."""
        raise NotImplementedError

    def modifica(self, **kwargs):
        """Update soggetto."""
        raise NotImplementedError

    def elimina(self, **kwargs):
        """Delete soggetto."""
        raise NotImplementedError


class Clienti(Soggetto):
    """Clienti class."""

    list_key = "lista_clienti"


class Fornitori(Soggetto):
    """Fornitori class."""

    list_key = "lista_fornitori"
