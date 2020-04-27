[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/python-page-object.svg?branch=master)](https://travis-ci.org/vyahello/python-page-object)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/python-page-object/badge.svg?branch=master)](https://coveralls.io/github/vyahello/python-page-object?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![GitHub version](https://badge.fury.io/gh/vyahello%2Fpython-page-object.svg)](https://github.com/vyahello/python-page-object/releases)
[![GitHub watchers](https://img.shields.io/github/watchers/vyahello/python-page-object.svg)](https://GitHub.com/vyahello/python-page-object/graphs/watchers/)
[![Forks](https://img.shields.io/github/forks/vyahello/python-page-object)](https://github.com/vyahello/python-page-object/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/python-page-object)](https://github.com/vyahello/python-page-object/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/python-page-object.svg)](https://GitHub.com/vyahello/python-page-object/graphs/contributors/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/python-page-object)](https://hitsofcode.com/view/github/vyahello/python-page-object)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/python-page-object/badge)](https://www.codefactor.io/repository/github/vyahello/python-page-object)

# Python page object model (PyPOM)
> Represent most popular OOD pattern for Web UI automation using python programming language (for learning reference only).
>
> Automated tests are demonstrated on http://newtours.demoaut.com/mercurywelcome.php web application. 

**Tools**
- python 3.6 | python 3.7 | python 3.8
- [pytest](https://pypi.org/project/pytest/) framework
- [selenium](https://selenium.dev/) library and [pom](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html) framework
- [allure](https://docs.qameta.io/allure/) reporting
- [travis](https://travis-ci.org/) CI
- code analysis
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [black](https://black.readthedocs.io/en/stable/)
  - [flake8](http://flake8.pycqa.org/en/latest/)

In addition code is **fully** [type annotated](https://docs.python.org/3/library/typing.html) ⭐

## Quick start
From the root directory of your shell run following commands:

- Smoke tests
```bash
./run-tests.sh smoke
```

- Unit tests
```bash
./run-tests.sh unit
```

- Whole suite
```bash
./run-tests.sh all
```

### Tests (html) report sample
Run a bunch of tests (e.g smoke) via following command:
```bash
./run-tests.sh smoke
```

After please open `test-report.html` file to see detailed testing report:

![Screenshot](demoauto/image/report.png)

### Generate allure report
Please follow next instruction to generate allure report (mac OS example):
1. Update java via `brew cask install adoptopenjdk`
2. Install allure via `brew install allure`
3. Generate allure project via `allure serve report`

![Screenshot](demoauto/image/allure.png)

## Development notes

### Release History

* 0.3.0
    * Introduce allure integration
* 0.2.0
    * Introduce travis CI
    * Add static code analysis tools (`black`, `flake8` and `mypy`) along with unittests
* 0.1.0
    * Distribute initial version

### Meta
Author – _Volodymyr Yahello_.

Distributed under the `GPL v3` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all project development dependencies
