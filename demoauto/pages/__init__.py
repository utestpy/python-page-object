from abc import ABC, abstractmethod
from demoauto.driver.driver import Driver
from demoauto.map.urls import Url


class Page(ABC):
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
