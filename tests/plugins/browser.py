import pytest
from _pytest.fixtures import SubRequest
from web.browsers.chrome import WebBrowser, Chrome


@pytest.fixture(scope='module')
def browser(request: SubRequest) -> WebBrowser:
    browser = Chrome()
    request.addfinalizer(browser.close)
    return browser
