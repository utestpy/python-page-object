import pytest
from web.browsers import WebBrowser
from web.pages import Page
from web.pages.home import HomePage


@pytest.fixture(scope='module')
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)
