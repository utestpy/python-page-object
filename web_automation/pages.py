from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Callable
from selenium.webdriver.common.by import By
from web_automation.elements import Element
from web_automation.locators import HomePage as HP_Locators
from web_automation.drivers import Driver, WebBrowserDriver
from web_automation.browsers import ChromeBrowser


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
        self.driver: Callable[..., Driver] = open_page

    def open_page(self, url: str = None) -> Driver:
        if not url:
            url: str = self._url
        return self.driver().get(url)


class HomePage(WebPage):
    """Represent home page."""

    def __init__(self) -> None:
        self._hp_locators: HP_Locators = HP_Locators
        self._page: WebPage = BasePage('http://newtours.demoaut.com/mercurywelcome.php')

    def open_page(self, url: str = None) -> None:
        self._page.open_page(url)

    def logo(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._hp_locators.logo)

    def contact(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._hp_locators.contact)
