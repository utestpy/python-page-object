class HomePage(object):
    """Represent home page web element locators."""

    logo: str = "//img[@alt='Mercury Tours']"
    sing_on: str = "//a[contains(text(), 'SIGN-ON')]"
    register: str = "//a[contains(text(), 'REGISTER')]"
    support: str = "//a[contains(text(), 'SUPPORT')]"
    contact: str = "//a[contains(text(), 'CONTACT')]"


class RegistrationPage(object):
    """Represent registration page web element locators."""

    regis_txt: str = "//*[contains(text(), 'basic information')]"
    first_name: str = "//input[@name='firstName']"
    last_name: str = "//input[@name='lastName']"
    phone: str = "//input[@name='phone']"
    email: str = "//input[@name='email']"
    country: str = "//input[@name='country']"
    userName: str = "//input[@name='userName']"
    password: str = "//input[@name='password']"
    confirm_password: str = "//input[@name='confirmPassword']"
    submit: str = "//input[@name='register']"


class PostRegistrationPage(object):
    """Represent post registration page web element locators."""

    thank_you: str = "//*[contains(text(), 'Thank you for registrating')]"
    post_user: str = "//*[contains(text(), 'Your user name is')]"


class SingOnPage(object):
    """Represent sign on page web element locators."""

    sign_on_user_name: str = "//input[@name='userName']"
    sign_on_password: str = "//input[@name='password']"
    sign_on_login: str = "//input[@name='login']"
    sign_on_txt: str = "//*[contains(text(), 'Enter your user')]"
    sign_on_register_link: str = "//a[@href='mercuryregister.php']"
