from typing import Callable
import pytest
from tests.coverage.markers import unittest
from lib.browsers import WebBrowser, WebBrowserError


@unittest
@pytest.mark.parametrize("name", [
    'Safari', 'Chrome'
])
def test_browser_name(browser: Callable[[str], WebBrowser], name: str) -> None:
    assert browser(name).name() == name


@unittest
def test_browser_error():
    with pytest.raises(WebBrowserError):
        raise WebBrowserError('Raised WebBrowserError!')
