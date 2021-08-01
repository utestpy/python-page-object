from abc import ABC, abstractmethod


BASE_DEMO_URL = "http://demo.guru99.com/test/newtours"


class Url(ABC):
    """Abstraction of a page url."""

    @abstractmethod
    def get(self) -> str:
        pass


class PageUrl(Url):
    """Represent web page url."""

    def __init__(self, url: str) -> None:
        self._url: str = url

    def get(self) -> str:
        return self._url


class HomePageUrl(Url):
    """Represent home page url."""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{BASE_DEMO_URL}/index.php")

    def get(self) -> str:
        return self._url.get()


class RegisterPageUrl(Url):
    """Represent register page url."""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{BASE_DEMO_URL}/register.php")

    def get(self) -> str:
        return self._url.get()


class SignOnPageUrl(Url):
    """Represent sign on page url."""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{BASE_DEMO_URL}/login.php")

    def get(self) -> str:
        return self._url.get()
