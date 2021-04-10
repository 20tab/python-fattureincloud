"""Utils about mocking."""


def mocked_text(filename):
    """Return json text from file."""

    with open(filename, "r") as f:
        return f.read()


def mocker_register_uri(mocker, host, path, filename):
    """Mock specific uri."""
    text = mocked_text(f"tests/responses/{filename}")
    mocker.register_uri("POST", f"{host}{path}", text=text)
