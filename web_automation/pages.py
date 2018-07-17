from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Callable
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from web_automation.locators import HomePage as HP_Locators
from web_automation.drivers import Driver, ChromeBrowser, WebBrowserDriver


class WebPage(ABC):
    """Abstraction of a web page."""

    @abstractmethod
    def open_page(self, url: str = None) -> None:
        pass


class BasePage(WebPage):
    """Represent base page."""

    def __init__(self, url: str) -> None:

        @lru_cache(typed=True)
        def open_page() -> Driver:
            return WebBrowserDriver(ChromeBrowser()).get(url)

        self._url: str = url
        self._driver: Callable[..., Driver] = open_page

    @property
    def driver(self) -> Driver:
        return self._driver()

    def open_page(self, url: str = None) -> None:
        if not url:
            url: str = self._url
        return self.driver.get(url)


class HomePage(WebPage):
    """Represent home page."""

    def __init__(self) -> None:
        self._hp_locators: HP_Locators = HP_Locators
        self._page: WebPage = BasePage('http://newtours.demoaut.com/mercurywelcome.php')

    def open_page(self, url: str = None) -> None:
        self._page.open_page(url)

    def get_logo(self) -> WebElement:
        return self._page.driver.find_element(By.XPATH, self._hp_locators.logo)

    def get_contact(self) -> WebElement:
        return self._page.driver.find_element(By.XPATH, self._hp_locators.contact)
