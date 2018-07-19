from abc import ABC, abstractmethod
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Condition(ABC):
    """Abstraction of web element condition."""

    @abstractmethod
    def presence_of_element_located(self) -> presence_of_element_located:
        pass


class ExpectedCondition(Condition):
    """Represent expected conditon of a web element."""

    def __init__(self, *locators: str) -> None:
        self._presence_of_element_located = presence_of_element_located(locators)

    def presence_of_element_located(self) -> presence_of_element_located:
        return self._presence_of_element_located
