import pytest
from demo.browsers import WebBrowser
from demo.pages import Page
from demo.pages.home import HomePage
from demo.pages.register import RegisterPage


@pytest.fixture(scope="module")
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope="module")
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
