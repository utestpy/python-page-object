from typing import Any
from demoauto.driver.driver import Driver
from demoauto.map.elements import Element, WebElement


class WebDriverOf(Driver):
    """Represent selenium web driver object."""

    def __init__(self, driver: Any) -> None:
        self._driver = driver

    def get(self, url: str) -> None:
        self._driver.get(url)

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self._driver.set_page_load_timeout(time_to_wait)

    def find_element(self, by_: str, locator: str) -> Element:
        return WebElement(self._driver.find_element(by_, locator))

    def implicitly_wait(self, time_to_wait: int) -> None:
        self._driver.implicitly_wait(time_to_wait)

    def maximize_window(self) -> None:
        self._driver.maximize_window()

    def close(self) -> None:
        self._driver.close()
        self._driver.quit()
