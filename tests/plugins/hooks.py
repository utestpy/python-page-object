from typing import List
from _pytest.config import Config


def pytest_configure(config: Config):
    """Enable verbose and output when running tests. Simulate `-v` and `-s` option in a command line."""

    config.option.verbose = 1
    config.option.capture = "yes"


def pytest_report_header(config: Config) -> List[str]:
    """Add information to test report header."""

    if config.option.verbose > 0:
        return [
            "Project: Pytest Page Object Model",
            "Written by: Volodymyr Yahello",
        ]
