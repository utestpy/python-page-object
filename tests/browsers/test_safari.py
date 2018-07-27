import pytest
from _pytest.fixtures import SubRequest
from web.browsers import WebBrowser
from web.browsers.safari import Safari


@pytest.fixture(scope='module')
def safari() -> WebBrowser:
    return Safari()


@pytest.fixture(scope='module', autouse=True)
def teardown_safari(safari: WebBrowser, request: SubRequest) -> None:
    request.addfinalizer(safari.close)


def test_name(safari: WebBrowser) -> None:
    assert safari.name() == 'Safari'
