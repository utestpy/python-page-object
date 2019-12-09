from tests.coverage.markers import smoke
from demoauto.pages.home import HomePage


@smoke
def test_home_page_logo(home_page: HomePage) -> None:
    assert home_page.logo().is_displayed()


@smoke
def test_home_page_contact(home_page: HomePage) -> None:
    assert home_page.contact().is_displayed()


@smoke
def test_home_page_sign_on(home_page: HomePage) -> None:
    assert home_page.sign_on().is_displayed()


@smoke
def test_home_page_support(home_page: HomePage) -> None:
    assert home_page.support().is_displayed()


@smoke
def test_home_page_register(home_page: HomePage) -> None:
    assert home_page.register().is_displayed()
