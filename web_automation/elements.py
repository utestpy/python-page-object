from abc import ABC, abstractmethod
from typing import Dict, Any
from selenium.webdriver.remote import webelement


class Element(ABC):
    """Abstraction of a web element."""

    @abstractmethod
    def text(self) -> str:
        pass

    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def size(self) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def location(self) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def send_keys(self, value: str) -> None:
        pass

    @abstractmethod
    def tag_name(self) -> str:
        pass

    @abstractmethod
    def click(self) -> None:
        pass


class WebElement(Element):
    """Represent concrete web element."""

    def __init__(self, element: webelement.WebElement) -> None:
        self._element = element

    def text(self) -> str:
        return self._element.text

    def id(self) -> str:
        return self._element.id

    def size(self) -> Dict[Any, Any]:
        return self._element.size

    def location(self) -> Dict[Any, Any]:
        return self._element.location

    def clear(self) -> None:
        self._element.clear()

    def send_keys(self, value: str) -> None:
        self._element.send_keys(value)

    def tag_name(self) -> str:
        return self._element.tag_name

    def click(self) -> None:
        self._element.click()
