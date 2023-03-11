from selenium.webdriver.support.select import Select
from demoauto.browsers import WebBrowser
from demoauto.map.conditions import ExpectedCondition
from demoauto.driver.driver import Driver
from demoauto.map.elements import Element
from demoauto.map.handlers import HandlerBy, WebHandlerBy
from demoauto.input.register import RegisterPageInput
from demoauto.locators.register import RegistrationPage as RP_Locators
from demoauto.pages import Page
from demoauto.pages.base import BasePage
from demoauto.map.urls import RegisterPageUrl, Url
from demoauto.map.waits import WebDriverWaitOf


class RegisterPage(Page):
    """Represent register page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._rp_locators: RP_Locators = RP_Locators()
        self._page: Page = BasePage(browser, RegisterPageUrl())

    @property
    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def register_text(self) -> Element:
        return self.driver.find_element(
            self._by.xpath(), self._rp_locators.regis_txt
        )

    def set_first_name(self, input_: RegisterPageInput) -> Element:
        first_name: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.first_name
        )
        first_name.clear()
        first_name.send_keys(input_.first_name)
        return first_name

    def set_last_name(self, input_: RegisterPageInput) -> None:
        last_name: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.last_name
        )
        last_name.clear()
        last_name.send_keys(input_.last_name)

    def set_phone(self, input_: RegisterPageInput) -> None:
        phone: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.phone
        )
        phone.clear()
        phone.send_keys(input_.phone)

    def set_email(self, input_: RegisterPageInput) -> None:
        email: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.email
        )
        email.clear()
        email.send_keys(input_.email)

    def set_country(self, input_: RegisterPageInput) -> None:
        select = Select(
            self.driver.find_element(
                self._by.xpath(), self._rp_locators.country
            ).element()
        )
        select.select_by_visible_text(input_.country)

    def set_user_name(self, input_: RegisterPageInput) -> None:
        user_name: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.user_name
        )
        user_name.clear()
        user_name.send_keys(input_.user_name)

    def set_password(self, input_: RegisterPageInput) -> None:
        password: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.password
        )
        password.clear()
        password.send_keys(input_.password)

    def confirm_password(self, input_: RegisterPageInput) -> None:
        confirm_password: Element = self.driver.find_element(
            self._by.xpath(), self._rp_locators.confirm_password
        )
        confirm_password.clear()
        confirm_password.send_keys(input_.password)

    def submit(self) -> None:
        self.driver.find_element(
            self._by.xpath(), self._rp_locators.submit
        ).click()

    def confirm_registration(self) -> Element:
        return WebDriverWaitOf(
            driver=self.driver, timeout=30
        ).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._rp_locators.thank_you)
        )
