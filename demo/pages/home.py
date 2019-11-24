from demo.browsers import WebBrowser
from demo.driver.driver import Driver
from demo.map.elements import Element
from demo.map.handlers import HandlerBy, WebHandlerBy
from demo.locators.home import HomePage as HP_Locators
from demo.pages import Page
from demo.pages.base import BasePage
from demo.map.urls import HomePageUrl, Url


class HomePage(Page):
    """Represent home page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._hp_locators: HP_Locators = HP_Locators()
        self._page: Page = BasePage(browser, HomePageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def logo(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.logo)

    def contact(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.contact)

    def sign_on(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.sing_on)

    def support(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.support)

    def register(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.register)
