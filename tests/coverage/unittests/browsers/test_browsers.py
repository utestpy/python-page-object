import pytest
from tests.coverage.markers import unittest
from demo.browsers import WebBrowserError


@unittest
def test_browser_error() -> None:
    with pytest.raises(WebBrowserError):
        raise WebBrowserError("Raised WebBrowserError!")
