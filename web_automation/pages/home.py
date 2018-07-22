from web_automation.browsers import WebBrowser
from web_automation.drivers import Driver
from web_automation.elements import Element
from web_automation.handlers import HandlerBy, WebHandlerBy
from web_automation.locators.home import HomePage as HP_Locators
from web_automation.pages import WebPage
from web_automation.pages.base import BasePage
from web_automation.urls import HomePageUrl, Url


class HomePage(WebPage):
    """Represent home page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._hp_locators: HP_Locators = HP_Locators
        self._page: WebPage = BasePage(browser, HomePageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def logo(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._hp_locators.logo)

    def contact(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._hp_locators.contact)

    def sign_on(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._hp_locators.sing_on)

    def support(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._hp_locators.support)

    def register(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._hp_locators.register)