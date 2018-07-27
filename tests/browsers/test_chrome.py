import pytest
from _pytest.fixtures import SubRequest
from web.browsers import WebBrowser
from web.browsers.chrome import Chrome


@pytest.fixture(scope='module')
def chrome() -> WebBrowser:
    return Chrome()


@pytest.fixture(scope='module', autouse=True)
def teardown_chrome(chrome: WebBrowser, request: SubRequest) -> None:
    request.addfinalizer(chrome.close)


def test_name(chrome: WebBrowser) -> None:
    assert chrome.name() == 'Chrome'
