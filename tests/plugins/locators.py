import pytest
from lib.locators.register import RegistrationPage


@pytest.fixture(scope='module')
def register_page_locator() -> RegistrationPage:
    return RegistrationPage()
