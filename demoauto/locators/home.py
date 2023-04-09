class HomePage:
    """Represent home page web element locators."""

    logo: str = "//img[@alt='Mercury Tours']"
    sing_on: str = "//a[contains(text(), 'SIGN-ON')]"
    register: str = "//a[contains(text(), 'REGISTER')]"
    support: str = "//a[contains(text(), 'SUPPORT')]"
    contact: str = "//a[contains(text(), 'CONTACT')]"
