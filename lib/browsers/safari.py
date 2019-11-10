from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from lib.browsers import WebBrowser
from lib.driver.web_driver import WebDriverOf
from lib.driver.driver import Driver


class Safari(WebBrowser):
    """Representation of a safari web browser."""

    def __init__(self) -> None:
        self._safari: WebDriver = webdriver.Safari()

    def driver(self) -> Driver:
        return WebDriverOf(self._safari)

    def name(self) -> str:
        return "Safari"
