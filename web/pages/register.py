from selenium.webdriver.support.select import Select
from web.browsers import WebBrowser
from web.map.conditions import ExpectedCondition
from web.driver.driver import Driver
from web.map.elements import Element
from web.map.handlers import HandlerBy, WebHandlerBy
from web.input.register import RegisterPageInput
from web.locators.register import RegistrationPage as RP_Locators
from web.pages import Page
from web.pages.base import BasePage
from web.map.urls import RegisterPageUrl, Url
from web.map.waits import WebDriverWaitOf


class RegisterPage(Page):
    """Represent register page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._rp_locators: RP_Locators = RP_Locators
        self._page: Page = BasePage(browser, RegisterPageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def register_text(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._rp_locators.regis_txt)

    def set_first_name(self, inp: RegisterPageInput) -> Element:
        first_name: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.first_name)
        first_name.clear()
        first_name.send_keys(inp.first_name)
        return first_name

    def set_last_name(self, inp: RegisterPageInput) -> None:
        last_name: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.last_name)
        last_name.clear()
        last_name.send_keys(inp.last_name)

    def set_phone(self, inp: RegisterPageInput) -> None:
        phone: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.phone)
        phone.clear()
        phone.send_keys(inp.phone)

    def set_email(self, inp: RegisterPageInput) -> None:
        email: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.email)
        email.clear()
        email.send_keys(inp.email)

    def set_country(self, inp: RegisterPageInput) -> None:
        select = Select(self.driver().find_element(self._by.xpath(), self._rp_locators.country).element())
        select.select_by_visible_text(inp.country)

    def set_user_name(self, inp: RegisterPageInput) -> None:
        user_name: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.user_name)
        user_name.clear()
        user_name.send_keys(inp.user_name)

    def set_password(self, inp: RegisterPageInput) -> None:
        password: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.password)
        password.clear()
        password.send_keys(inp.password)

    def confirm_password(self, inp: RegisterPageInput) -> None:
        confirm_password: Element = self.driver().find_element(self._by.xpath(), self._rp_locators.confirm_password)
        confirm_password.clear()
        confirm_password.send_keys(inp.password)

    def submit(self) -> None:
        self.driver().find_element(self._by.xpath(), self._rp_locators.submit).click()

    def confirm_registration(self) -> Element:
        return WebDriverWaitOf(
            driver=self.driver(), timeout=15).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._rp_locators.thank_you))
