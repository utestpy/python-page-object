from abc import ABC, abstractmethod
from selenium.webdriver import Chrome, Firefox, Safari
from selenium.webdriver.chrome.webdriver import WebDriver


class WebBrowser(ABC):
    """Abstraction of a web browser."""

    @abstractmethod
    def driver(self) -> WebDriver:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class ChromeBrowser(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        self._browser: WebDriver = Chrome()

    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Chrome'


class FireFoxBrowser(WebBrowser):
    """Representation of a firefox web browser."""

    def __init__(self) -> None:
        self._browser: WebDriver = Firefox()

    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Firefox'


class SafariBrowser(WebBrowser):
    """Representation of a safari web browser."""

    def __init__(self) -> None:
        self._browser: WebDriver = Safari()

    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Safari'
