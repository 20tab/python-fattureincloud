"""Utils about mocking."""


def mocked_text(filename):
    """Return json text from file."""

    with open(filename, "r") as f:
        return f.read()


def mocker_register_uri(mocker, host, path, filename):
    """Mock specific uri."""
    text = mocked_text(f"tests/responses/{filename}")
    mocker.register_uri("POST", f"{host}{path}", text=text)


class MockedErrorResponse:
    """Define mocked error response."""

    def __init__(self):
        """Set error status code."""
        self.status_code = 500
        self.content = ""
