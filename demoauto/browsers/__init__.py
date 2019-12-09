from abc import ABC, abstractmethod
from demoauto.driver.driver import Driver


class WebBrowser(ABC):
    """Abstraction of a web browser."""

    @abstractmethod
    def driver(self) -> Driver:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class WebBrowserError(Exception):
    """Represent web browser error."""

    pass
