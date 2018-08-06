from typing import Callable
import pytest
from web.browsers import WebBrowser, WebBrowserError


@pytest.mark.unittest
@pytest.mark.parametrize("name", [
    'Safari', 'Chrome'
])
def test_browser_name(browser: Callable[[str], WebBrowser], name: str) -> None:
    assert browser(name).name() == name


@pytest.mark.unittest
def test_browser_error():
    with pytest.raises(WebBrowserError):
        raise WebBrowserError('Raised WebBrowserError!')
