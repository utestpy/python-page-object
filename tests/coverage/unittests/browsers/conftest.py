from typing import Callable
import pytest
from _pytest.fixtures import SubRequest
from web.browsers import WebBrowser, WebBrowserError
from web.browsers.chrome import Chrome
from web.browsers.safari import Safari


@pytest.fixture
def browser(request: SubRequest) -> Callable[[str], WebBrowser]:
    def browser_factory(name: str) -> WebBrowser:
        request.addfinalizer(lambda: target.driver().close())
        if name == 'Chrome':
            target = Chrome()
            return target
        if name == 'Safari':
            target = Safari()
            return target
        raise WebBrowserError(f'Browser {name} is not supported!')
    return browser_factory
