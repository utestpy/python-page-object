import pytest
from _pytest.fixtures import SubRequest
from demo.browsers.chrome import WebBrowser, Chrome


@pytest.fixture(scope="module")
def browser(request: SubRequest) -> WebBrowser:
    browser = Chrome()
    request.addfinalizer(browser.driver().close)
    return browser
