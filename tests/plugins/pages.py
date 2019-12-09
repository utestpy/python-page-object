import pytest
from demoauto.browsers import WebBrowser
from demoauto.pages import Page
from demoauto.pages.home import HomePage
from demoauto.pages.register import RegisterPage


@pytest.fixture(scope="module")
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope="module")
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
