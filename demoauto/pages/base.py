from functools import lru_cache
from typing import Callable, Optional
from demoauto.browsers import WebBrowser
from demoauto.driver.driver import Driver
from demoauto.pages import Page
from demoauto.map.urls import Url


class BasePage(Page):
    """Represent base page."""

    def __init__(self, browser: WebBrowser, url: Url) -> None:
        @lru_cache(maxsize=128)
        def _driver() -> Driver:
            driver: Driver = browser.driver()
            driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.get(url.get())
            return driver

        self._url: Url = url
        self._driver: Callable[..., Driver] = _driver

    def driver(self) -> Driver:
        return self._driver()

    def open(self, url: Optional[Url] = None) -> None:
        if not url:
            url = self._url
        self._driver().get(url.get())

    def close(self) -> None:
        self._driver().close()
