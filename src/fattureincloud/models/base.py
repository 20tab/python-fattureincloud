"""Define Resources."""


class Resource:
    """Define base resource class."""

    def __init__(self, requester):
        """Set requester."""
        cname = self.__class__.__name__.lower()
        self.path = f"/{cname}/"
        self.requester = requester
