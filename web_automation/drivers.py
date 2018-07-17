from abc import ABC, abstractmethod
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome, Firefox, Safari
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Driver(ABC):
    """Abstraction of a web driver."""

    @abstractmethod
    def get(self, url: str) -> None:
        pass

    @abstractmethod
    def set_page_load_timeout(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def implicitly_wait(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def find_element(self, by: str, value: str) -> WebElement:
        pass

    @abstractmethod
    def maximize_window(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


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

    @property
    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Chrome'


class FireFoxBrowser(WebBrowser):
    """Representation of a firefox web browser."""

    def __init__(self) -> None:
        self._browser: WebDriver = Firefox()

    @property
    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Firefox'


class SafariBrowser(WebBrowser):
    """Representation of a safari web browser."""

    def __init__(self) -> None:
        self._browser: WebDriver = Safari()

    @property
    def driver(self) -> WebDriver:
        return self._browser

    def name(self) -> str:
        return 'Safari'


class WebDriverOf(Driver):
    """A singleton selenium web driver object."""

    def __new__(cls, web_browser: WebBrowser) -> WebDriver:
        if not hasattr(cls, '_driver'):
            cls._driver: WebDriver = web_browser.driver
        return cls._driver

    def find_element(self, by: str, locator: str) -> WebElement:
        return self._driver.find_element(By, locator)

    def get(self, url: str) -> Driver:
        self._driver.get(url)
        return self

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self._driver.set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait: int) -> None:
        self._driver.implicitly_wait(time_to_wait)

    def maximize_window(self) -> None:
        self._driver.maximize_window()

    def close(self) -> None:
        self._driver.close()
        self._driver.quit()


class WebBrowserDriver(Driver):
    """Representation of a web browser driver."""

    def __init__(self, browser: WebBrowser) -> None:
        self._driver: Driver = WebDriverOf(browser)

    def find_element(self, by: str, locator: str) -> WebElement:
        return self._driver.find_element(by, locator)

    def get(self, url: str) -> Driver:
        self._driver.get(url)
        return self

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self._driver.set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait: int) -> None:
        self._driver.implicitly_wait(time_to_wait)

    def maximize_window(self) -> None:
        self._driver.maximize_window()

    def close(self) -> None:
        self._driver.close()
