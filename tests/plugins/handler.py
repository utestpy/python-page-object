import pytest
from demo.map.handlers import HandlerBy, WebHandlerBy


@pytest.fixture(scope="module")
def handler_by() -> HandlerBy:
    return WebHandlerBy()
