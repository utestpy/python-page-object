# Page object design pattern implementation in python
> Represent most popular OOD pattern for Web UI automation using python programming language.
>
> Automated tests are demonstrated on http://newtours.demoaut.com/mercurywelcome.php web app. Enjoy it!

[![Build Status](https://travis-ci.org/vyahello/python-page-object.svg?branch=master)](https://travis-ci.org/vyahello/python-page-object)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/python-page-object/badge.svg?branch=master)](https://coveralls.io/github/vyahello/python-page-object?branch=master)

**Tools**
> - `python 3.6+`
> - `selenium` and `pom`
> - `pytest`

## Run automated tests
From the root directory of your shell run following commands:

**Smoke tests**
```bash
~ ./run-tests.sh smoke
```

**Unit tests**
```bash
~ ./run-tests.sh unittest
```

**Launch whole set of tests**
```bash
~ ./run-tests.sh all
```

### Tests report sample
Run a bunch of tests via following command:
```bash
~ ./run-tests.sh smoke
```

After please open `test-report.html` file to see detailed testing report:

![Screenshot](image/report.png)

## Release History

* 0.1.0
    * Distribute initial version

## Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies