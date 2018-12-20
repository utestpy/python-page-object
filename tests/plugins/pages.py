import pytest
from lib.browsers import WebBrowser
from lib.pages import Page
from lib.pages.home import HomePage
from lib.pages.register import RegisterPage


@pytest.fixture(scope='module')
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope='module')
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
