from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Callable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web_automation.elements import Element
from web_automation.locators import HomePage as HP_Locators, RegistrationPage as RP_Locators
from web_automation.drivers import Driver, WebDriverOf
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
            driver: Driver = WebDriverOf(ChromeBrowser())
            driver.get(url)
            return driver

        self._url: str = url
        self.driver: Callable[..., Driver] = open_page

    def open_page(self, url: str = None) -> Driver:
        if not url:
            url: str = self._url
        self.driver().get(url)
        return self.driver()


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

    def sign_on(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._hp_locators.sing_on)

    def support(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._hp_locators.support)

    def register(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._hp_locators.register)


class RegisterPage(WebPage):
    """Represent register page."""

    def __init__(self) -> None:
        self._rp_locators: RP_Locators = RP_Locators
        self._page: WebPage = BasePage('http://newtours.demoaut.com/mercuryregister.php')

    def open_page(self, url: str = None) -> None:
        self._page.open_page(url)

    def regis_txt(self) -> Element:
        return self._page.driver().find_element(By.XPATH, self._rp_locators.regis_txt)

    def set_first_name(self, value: str) -> None:
        first_name: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.first_name)
        first_name.clear()
        first_name.send_keys(value)

    def set_last_name(self, value: str) -> None:
        last_name: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.last_name)
        last_name.clear()
        last_name.send_keys(value)

    def set_phone(self, value: str) -> None:
        phone: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.phone)
        phone.clear()
        phone.send_keys(value)

    def set_email(self, value: str) -> None:
        email: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.email)
        email.clear()
        email.send_keys(value)

    def set_country(self, value: str) -> None:
        select = Select(self._page.driver().find_element(By.XPATH, self._rp_locators.country))
        select.select_by_visible_text(value)

    def set_user_name(self, value: str) -> None:
        user_name: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.user_name)
        user_name.clear()
        user_name.send_keys(value)

    def set_password(self, value: str) -> None:
        password: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.password)
        password.clear()
        password.send_keys(value)

    def confirm_password(self, value: str) -> None:
        confirm_password: Element = self._page.driver().find_element(By.XPATH, self._rp_locators.confirm_password)
        confirm_password.clear()
        confirm_password.send_keys(value)

    def submit(self) -> None:
        self._page.driver().find_element(By.XPATH, self._rp_locators.submit).click()
