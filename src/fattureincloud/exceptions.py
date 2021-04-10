"""Exception definitions."""


class FattureInCloudExcpetion(Exception):
    """FattureInCloudError class."""

    def __init__(self, message="", status_code=None, body=None):
        """Create FattureInCloudExcpetion instance."""
        Exception.__init__(self, message)
        self.status_code = status_code
        self.body = body
        try:
            self.message = message.decode()
        except Exception:
            self.message = message

    def __str__(self):
        """Represent exception instance."""

        if self.status_code is not None:
            return "{0}: {1}".format(self.status_code, self.message)
        else:
            return "{0}".format(self.message)
