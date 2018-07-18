from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By


class HandlerBy(ABC):
    """Abstraction of a handler."""

    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def xpath(self) -> str:
        pass

    @abstractmethod
    def link_text(self) -> str:
        pass

    @abstractmethod
    def partial_link_text(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def tag_name(self) -> str:
        pass

    @abstractmethod
    def class_name(self) -> str:
        pass

    @abstractmethod
    def css_selector(self) -> str:
        pass


class WebHandlerBy(HandlerBy):
    """Represent web handler search."""

    def __init__(self) -> None:
        self._by: By = By()

    def id(self) -> str:
        return self._by.ID

    def xpath(self) -> str:
        return self._by.XPATH

    def link_text(self) -> str:
        return self._by.LINK_TEXT

    def partial_link_text(self) -> str:
        return self._by.PARTIAL_LINK_TEXT

    def name(self) -> str:
        return self._by.NAME

    def tag_name(self) -> str:
        return self._by.TAG_NAME

    def class_name(self) -> str:
        return self._by.CLASS_NAME

    def css_selector(self) -> str:
        return self._by.CSS_SELECTOR
