class RegisterPageInput(object):
    """Represent register page input data."""

    first_name: str = 'Volodymyr'
    last_name: str = 'Yahello'
    phone: str = '+709-319-789'
    email: str = 'fancy_world@gmail.com'
    country: str = 'Ukraine'
    user_name: str = 'vyahello'
    password: str = 'password'


class SignOnPageInput(object):
    """Represent sign on page input data."""

    user_name: str = 'vyahello'
    password: str = 'password'
