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
        return self.requester.post(f"{self.path}lista", payload)

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

    def lista(self, **kwargs):
        """Return list of Clienti filtered by given parameters if set."""
        return super().lista(**kwargs).get("lista_clienti", [])


class Fornitori(Soggetto):
    """Fornitori class."""

    def lista(self, **kwargs):
        """Return list of Fornitori filtered by given parameters if set."""
        return super().lista(**kwargs).get("lista_fornitori", [])
