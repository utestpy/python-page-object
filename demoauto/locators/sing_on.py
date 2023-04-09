class SingOnPage:
    """Represent sign on page web element locators."""

    user_name: str = "//input[@name='userName']"
    password: str = "//input[@name='password']"
    login: str = "//input[@name='login']"
    txt: str = "//*[contains(text(), 'Enter your user')]"
    register_link: str = "//*[starts-with(@href, 'mercuryregister.php')]"
