import pytest
from web.browsers import WebBrowser
from web.pages import Page
from web.pages.home import HomePage
from web.pages.register import RegisterPage


@pytest.fixture(scope='module')
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope='module')
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
