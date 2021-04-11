from unittest import TestCase

from fattureincloud.exceptions import FattureInCloudExcpetion


class TestFattureInCloudExcpetion(TestCase):
    """Define FattureInCloudExcpetion test case."""

    def test_complete_exception(self):
        """Test exception with filled fields."""
        exception = FattureInCloudExcpetion(
            message="error message", status_code=500, body="complete error message"
        )
        self.assertEqual(f"{exception}", "500: error message")

    def test_uncomplete_exception(self):
        """Test exception with not all filled fields."""
        exception = FattureInCloudExcpetion(message="error message")
        self.assertEqual(f"{exception}", "error message")
