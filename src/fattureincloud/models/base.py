"""Define Resources."""


class Resource:
    """Define base resource class."""

    def __init__(self, requester):
        """Set requester."""
        cname = self.__class__.__name__.lower()
        self.path = f"/{cname}/"
        self.requester = requester

    def lista(self, **kwargs):
        """Return list of elements filtered by given parameters if set."""
        res = self.requester.post(f"{self.path}lista", kwargs)
        result_list = res.get(self.list_key, [])
        current_page = res.get("pagina_corrente", 1)
        numero_pagine = res.get("numero_pagine", 1)

        while current_page < numero_pagine:
            kwargs["pagina"] = current_page + 1
            res = self.requester.post(f"{self.path}lista", kwargs)
            current_page += 1
            result_list.extend(res.get(self.list_key, []))
        return result_list
