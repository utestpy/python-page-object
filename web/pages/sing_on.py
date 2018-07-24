from web.browsers import WebBrowser
from web.conditions import ExpectedCondition
from web.drivers import Driver
from web.elements import Element
from web.handlers import HandlerBy, WebHandlerBy
from web.input.sign_on import SignOnPageInput
from web.locators.sing_on import SingOnPage as SP_Locators
from web.pages import Page
from web.pages.base import BasePage
from web.urls import SignOnPageUrl, Url
from web.waits import WebDriverWaitOf


class SignOnPage(Page):
    """Represent sign-on page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._sp_locators: SP_Locators = SP_Locators
        self._page: Page = BasePage(browser, SignOnPageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def user_name(self, inp: SignOnPageInput) -> None:
        field: Element = self._page.driver().find_element(self._by.xpath(), self._sp_locators.user_name)
        field.clear()
        field.send_keys(inp.user_name)

    def password(self, inp: SignOnPageInput) -> None:
        field: Element = self._page.driver().find_element(self._by.xpath(), self._sp_locators.password)
        field.clear()
        field.send_keys(inp.password)

    def text(self) -> Element:
        return WebDriverWaitOf(self._page.driver()).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._sp_locators.txt))

    def register_link(self) -> Element:
        return WebDriverWaitOf(self._page.driver()).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._sp_locators.register_link))

    def login(self) -> None:
        self._page.driver().find_element(self._by.xpath(), self._sp_locators.login).click()