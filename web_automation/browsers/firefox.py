from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from web_automation.browsers import WebBrowser
from web_automation.drivers import Driver, WebDriverOf


class FireFox(WebBrowser):
    """Representation of a firefox web browser."""

    def __init__(self) -> None:
        self._firefox: WebDriver = webdriver.Firefox()

    def driver(self) -> Driver:
        return WebDriverOf(self._firefox)

    def name(self) -> str:
        return 'Firefox'
