from web_automation.browsers import WebBrowser
from web_automation.conditions import ExpectedCondition
from web_automation.drivers import Driver
from web_automation.elements import Element
from web_automation.handlers import HandlerBy, WebHandlerBy
from web_automation.input.sign_on import SignOnPageInput
from web_automation.locators.sing_on import SingOnPage as SP_Locators
from web_automation.pages import WebPage
from web_automation.pages.base import BasePage
from web_automation.urls import SignOnPageUrl, Url
from web_automation.waits import WebDriverWaitOf


class SignOnPage(WebPage):
    """Represent sign-on page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._sp_locators: SP_Locators = SP_Locators
        self._page: WebPage = BasePage(browser, SignOnPageUrl())

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