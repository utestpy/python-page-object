from tests.coverage.markers import unit
from demoauto.map.urls import Url

_home: str = "http://newtours.demoaut.com/mercurywelcome.php"
_register: str = "http://newtours.demoaut.com/mercuryregister.php"
_sign_on: str = "http://newtours.demoaut.com/mercurysignon.php"


@unit
def test_home_url(home_url: Url) -> None:
    assert home_url.get() == _home


@unit
def test_register_url(register_url: Url) -> None:
    assert register_url.get() == _register


@unit
def test_sign_on_url(sign_on_url: Url) -> None:
    assert sign_on_url.get() == _sign_on
