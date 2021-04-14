"""Anagrafica app."""
from datetime import date

from fattureincloud.models.base import Resource


class Mail(Resource):
    """Mail class."""

    list_key = "lista_mail"

    def lista(
        self,
        filtro="",
        destinatario="",
        mittente="",
        stato="",
        data_inizio="",
        data_fine="",
        pagina=1,
    ):
        """Return list of elements filtered by given parameters if set."""
        payload = {
            "filtro": filtro,
            "destinatario": destinatario,
            "mittente": mittente,
            "stato": stato,
            "data_inizio": data_inizio
            or date(year=date.today().year, month=1, day=1).strftime("%d/%m/%Y"),
            "data_fine": data_fine
            or date(year=date.today().year, month=12, day=31).strftime("%d/%m/%Y"),
            "pagina": pagina,
        }
        return super().lista(**payload)
