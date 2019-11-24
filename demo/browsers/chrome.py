from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from demo.browsers import WebBrowser
from demo.driver.web_driver import WebDriverOf
from demo.driver.driver import Driver


class Chrome(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        self._chrome: WebDriver = webdriver.Chrome()

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"
