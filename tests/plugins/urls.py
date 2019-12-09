import pytest
from demoauto.map.urls import HomePageUrl, RegisterPageUrl, SignOnPageUrl, Url


@pytest.fixture(scope="module")
def home_url() -> Url:
    return HomePageUrl()


@pytest.fixture(scope="module")
def register_url() -> Url:
    return RegisterPageUrl()


@pytest.fixture(scope="module")
def sign_on_url() -> Url:
    return SignOnPageUrl()
