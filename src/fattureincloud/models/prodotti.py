"""Anagrafica app."""
from fattureincloud.models.base import Resource


class Prodotti(Resource):
    """Soggetto class."""

    def lista(
        self, _id="", filtro="", nome="", cod="", desc="", categoria="", pagina=1
    ):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "id": _id,
            "filtro": filtro,
            "nome": nome,
            "cod": cod,
            "desc": desc,
            "categoria": categoria,
            "pagina": pagina,
        }
        return self.requester.post(f"{self.path}lista", payload).get(
            "lista_prodotti", []
        )

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
