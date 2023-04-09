from abc import ABC, abstractmethod
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located as PresenceOfElement,
)


class Condition(ABC):
    """Abstraction of web element condition."""

    @abstractmethod
    def presence_of_element_located(self) -> PresenceOfElement:
        pass


class ExpectedCondition(Condition):
    """Represent expected condition of a web element."""

    def __init__(self, *locators: str) -> None:
        self._presence_of_element_located: PresenceOfElement = (
            PresenceOfElement(locators)
        )

    def presence_of_element_located(self) -> PresenceOfElement:
        return self._presence_of_element_located
