from functools import lru_cache
from typing import Callable
from web_automation.browsers import WebBrowser
from web_automation.drivers import Driver
from web_automation.pages import WebPage
from web_automation.urls import Url


class BasePage(WebPage):
    """Represent base page."""

    def __init__(self, browser: WebBrowser, url: Url) -> None:

        @lru_cache(maxsize=128)
        def _driver() -> Driver:
            driver: Driver = browser.driver()
            driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get(url.get())
            return driver

        self._url: str = url
        self._driver: Callable[..., Driver] = _driver

    def driver(self) -> Driver:
        return self._driver()

    def open(self, url: Url = None) -> None:
        if not url:
            url: Url = self._url
        self._driver().get(url.get())

    def close(self) -> None:
        self._driver().close()