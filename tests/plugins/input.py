import pytest
from demoauto.input.register import RegisterPageInput


@pytest.fixture(scope="module")
def register_page_input() -> RegisterPageInput:
    return RegisterPageInput()
