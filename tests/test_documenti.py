from requests_mock import Mocker

from tests.mocking import mocker_register_uri
from tests.test_client import TestClient


class TestDocumenti(TestClient):
    """Define simple test case for base client request."""

    @Mocker()
    def test_documenti_lista(self, mocker):
        """Test documenti lista."""
        documenti = [
            "fatture",
            "proforma",
            "ordini",
            "preventivi",
            "ndc",
            "ricevute",
            "ddt",
        ]
        for t in documenti:
            mocker_register_uri(
                mocker, self.client.host, f"/{t}/lista", f"documenti/{t}.json"
            )
            obj = getattr(self.client, t)
            self.assertEqual(len(obj.lista()), 2)

    @Mocker()
    def test_documenti_dettagli(self, mocker):
        """Test documenti dettagli."""
        documenti = [
            "fatture",
            "proforma",
            "ordini",
            "preventivi",
            "ndc",
            "ricevute",
            "ddt",
        ]
        for t in documenti:
            mocker_register_uri(
                mocker, self.client.host, f"/{t}/dettagli", "documenti/dettagli.json"
            )
            obj = getattr(self.client, t)
            details = obj.dettagli(_id=1, token="1234567890abcdefghijklmnopqrstuv")
            self.assertEqual(details.get("token"), "1234567890abcdefghijklmnopqrstuv")

    @Mocker()
    def test_documenti_info(self, mocker):
        """Test documenti info."""
        documenti = [
            "fatture",
            "proforma",
            "ordini",
            "preventivi",
            "ndc",
            "ricevute",
            "ddt",
        ]
        EXPECTED = {
            "ddt_numero_successivo": 1,
            "numerazioni": {"": 105},
            "default_id_template": "2821",
            "default_ddt_id_template": "3053",
            "default_ftacc_id_template": "3054",
            "default_cod_iva": 0,
            "default_note": "",
            "default_cassa_previdenziale": 0,
            "default_rivalsa_previdenziale": 0,
            "default_altra_ritenuta": 0,
            "default_ritenuta_acconto": 0,
            "default_imponibile_ritenuta": 100,
            "default_prezzi_ivati": False,
            "default_id_metodo_pagamento": 1269724,
        }
        for t in documenti:
            mocker_register_uri(
                mocker, self.client.host, f"/{t}/info", "documenti/info.json"
            )
            obj = getattr(self.client, t)
            info = obj.info(anno_competenza=2020)
            self.assertDictEqual(info, EXPECTED)

    @Mocker()
    def test_documenti_infomail(self, mocker):
        """Test documenti infomail."""
        documenti = [
            "fatture",
            "proforma",
            "ordini",
            "preventivi",
            "ndc",
            "ricevute",
            "ddt",
        ]
        EXPECTED = {
            "success": True,
            "mail_destinatario": "mario.rossi@example.it",
            "mail_mittente": [
                {"id": "0", "default": "true", "mail": "mio.indirizzo.invio@example.it"}
            ],
            "mail_cc": "mio.indirizzo@example.it",
            "oggetto_default": "Nostra fattura nr. 1",
            "messaggio_default": "Gentile Mario Rossi, ecco la nostra fattura.",
            "esiste_documento": True,
            "esiste_ddt": True,
            "esiste_fa": True,
            "esiste_allegato": True,
        }
        for t in documenti:
            mocker_register_uri(
                mocker, self.client.host, f"/{t}/infomail", "documenti/infomail.json"
            )
            obj = getattr(self.client, t)
            info = obj.infomail(_id=1, token="1234567890abcdefghijklmnopqrstuv")
            self.assertDictEqual(info, EXPECTED)
