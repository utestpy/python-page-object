from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Callable
from selenium.webdriver.support.select import Select
from web_automation.browsers import WebBrowser
from web_automation.conditions import ExpectedCondition
from web_automation.elements import Element
from web_automation.handlers import HandlerBy, WebHandlerBy
from web_automation.inputs import RegisterPageInput, SignOnPageInput
from web_automation.locators import (
    HomePage as HP_Locators,
    RegistrationPage as RP_Locators,
    SingOnPage as SP_Locators
)
from web_automation.drivers import Driver
from web_automation.urls import Url, HomePageUrl, RegisterPageUrl, SignOnPageUrl
from web_automation.waits import WebDriverWaitOf


class WebPage(ABC):
    """Abstraction of a web page."""

    @abstractmethod
    def driver(self) -> Driver:
        pass

    @abstractmethod
    def open(self, url: str = None) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class BasePage(WebPage):
    """Represent base page."""

    def __init__(self, browser: WebBrowser, url: Url) -> None:

        @lru_cache(maxsize=128)
        def _driver() -> Driver:
            driver = browser.driver()
            driver.get(url.get())
            return driver

        self._url: str = url
        self._driver: Callable[..., Driver] = _driver

    def driver(self) -> Driver:
        return self._driver()

    def open(self, url: str = None) -> None:
        if not url:
            url: str = self._url
        self._driver().get(url)

    def close(self) -> None:
        self._driver().close()


class HomePage(WebPage):
    """Represent home page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._hp_locators: HP_Locators = HP_Locators
        self._page: WebPage = BasePage(browser, HomePageUrl())

    def driver(self) -> None:
        self._page.driver()

    def open(self, url: str = None) -> None:
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


class RegisterPage(WebPage):
    """Represent register page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._rp_locators: RP_Locators = RP_Locators
        self._page: WebPage = BasePage(browser, RegisterPageUrl())

    def driver(self) -> None:
        self._page.driver()

    def open(self, url: str = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def regis_txt(self) -> Element:
        return self._page.driver().find_element(self._by.xpath(), self._rp_locators.regis_txt)

    def set_first_name(self, inp: RegisterPageInput) -> None:
        first_name: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.first_name)
        first_name.clear()
        first_name.send_keys(inp.first_name)

    def set_last_name(self, inp: RegisterPageInput) -> None:
        last_name: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.last_name)
        last_name.clear()
        last_name.send_keys(inp.last_name)

    def set_phone(self, inp: RegisterPageInput) -> None:
        phone: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.phone)
        phone.clear()
        phone.send_keys(inp.phone)

    def set_email(self, inp: RegisterPageInput) -> None:
        email: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.email)
        email.clear()
        email.send_keys(inp.email)

    def set_country(self, inp: RegisterPageInput) -> None:
        select = Select(self._page.driver().find_element(self._by.xpath(), self._rp_locators.country))
        select.select_by_visible_text(inp.country)

    def set_user_name(self, inp: RegisterPageInput) -> None:
        user_name: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.user_name)
        user_name.clear()
        user_name.send_keys(inp.user_name)

    def set_password(self, inp: RegisterPageInput) -> None:
        password: Element = self._page.driver().find_element(self._by.xpath(), self._rp_locators.password)
        password.clear()
        password.send_keys(inp.password)

    def confirm_password(self, inp: RegisterPageInput) -> None:
        confirm_password: Element = self._page.driver().find_element(self._by.xpath(),
                                                                     self._rp_locators.confirm_password)
        confirm_password.clear()
        confirm_password.send_keys(inp.password)

    def submit(self) -> None:
        self._page.driver().find_element(self._by.xpath(), self._rp_locators.submit).click()

    def confirm_registration(self) -> Element:
        return WebDriverWaitOf(self._page.driver()).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._rp_locators.thank_you))


class SignOnPage(WebPage):
    """Represent sign-on page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._sp_locators: SP_Locators = SP_Locators
        self._page: WebPage = BasePage(browser, SignOnPageUrl())

    def driver(self) -> None:
        self._page.driver()

    def open(self, url: str = None) -> None:
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
