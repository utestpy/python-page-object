from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from web_automation.browsers import WebBrowser
from web_automation.drivers import Driver, WebDriverOf


class Chrome(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        self._chrome: WebDriver = webdriver.Chrome()

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return 'Chrome'
