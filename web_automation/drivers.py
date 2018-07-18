from abc import ABC, abstractmethod
from typing import Callable
from selenium.webdriver.chrome import webdriver
from web_automation.browsers import WebBrowser
from web_automation.elements import Element, WebElement


class Driver(ABC):
    """Abstraction of a web driver."""

    @abstractmethod
    def get(self, url: str) -> 'Driver':
        pass

    @abstractmethod
    def set_page_load_timeout(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def implicitly_wait(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def find_element(self, by: str, value: str) -> Element:
        pass

    @abstractmethod
    def maximize_window(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class WebDriverOf(Driver):
    """A singleton selenium web driver object."""

    def __init__(self, web_browser: WebBrowser) -> None:
        self._driver: Callable[..., webdriver.WebDriver] = lambda: web_browser.driver()

    def find_element(self, by: str, locator: str) -> Element:
        return WebElement(self._driver().find_element(by, locator))

    def get(self, url: str) -> Driver:
        self._driver().get(url)
        return self

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self._driver().set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait: int) -> None:
        self._driver().implicitly_wait(time_to_wait)

    def maximize_window(self) -> None:
        self._driver().maximize_window()

    def close(self) -> None:
        self._driver().close()
        self._driver().quit()


class WebBrowserDriver(Driver):
    """Representation of a web browser driver."""

    def __init__(self, browser: WebBrowser) -> None:
        self._driver: Driver = WebDriverOf(browser)

    def find_element(self, by: str, locator: str) -> Element:
        return self._driver.find_element(by, locator)

    def get(self, url: str) -> Driver:
        return self._driver.get(url)

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self._driver.set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait: int) -> None:
        self._driver.implicitly_wait(time_to_wait)

    def maximize_window(self) -> None:
        self._driver.maximize_window()

    def close(self) -> None:
        self._driver.close()
