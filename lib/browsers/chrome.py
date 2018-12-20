from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from lib.browsers import WebBrowser
from lib.driver.web_driver import WebDriverOf
from lib.driver.driver import Driver


class Chrome(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        self._chrome: WebDriver = webdriver.Chrome()

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return 'Chrome'
