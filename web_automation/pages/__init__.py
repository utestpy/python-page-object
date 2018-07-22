from abc import ABC, abstractmethod
from web_automation.drivers import Driver
from web_automation.urls import Url


class WebPage(ABC):
    """Abstraction of a web page."""

    @abstractmethod
    def driver(self) -> Driver:
        pass

    @abstractmethod
    def open(self, url: Url = None) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass