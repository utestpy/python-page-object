import pytest
from web.map.handlers import HandlerBy, WebHandlerBy


@pytest.fixture(scope='module')
def handler_by() -> HandlerBy:
    return WebHandlerBy()
