from tests.coverage.markers import unit
from demoauto.map.urls import Url, BASE_DEMO_URL

_home: str = f"{BASE_DEMO_URL}/index.php"
_register: str = f"{BASE_DEMO_URL}/register.php"
_sign_on: str = f"{BASE_DEMO_URL}/login.php"


@unit
def test_home_url(home_url: Url) -> None:
    assert home_url.get() == _home


@unit
def test_register_url(register_url: Url) -> None:
    assert register_url.get() == _register


@unit
def test_sign_on_url(sign_on_url: Url) -> None:
    assert sign_on_url.get() == _sign_on
