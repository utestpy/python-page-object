![Screenshot](media/icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/python-page-object.svg?branch=master)](https://travis-ci.org/vyahello/python-page-object)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/python-page-object/badge.svg?branch=master)](https://coveralls.io/github/vyahello/python-page-object?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE.md)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/python-page-object/badge)](https://www.codefactor.io/repository/github/vyahello/python-page-object)
[![Docs](https://img.shields.io/badge/docs-github-orange)](https://vyahello.github.io/python-page-object)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)

# Python page object model (PyPOM)
> Represent most popular OOD pattern for Web UI automation using python programming language (for learning reference only).
>
> Automated tests are demonstrated on http://demo.guru99.com/test/newtours web application. 

## Tools

### Production
- python 3.6, 3.7, 3.8, 3.9
- [pytest](https://pypi.org/project/pytest/) framework
- [selenium](https://selenium.dev/) library
- [pom](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html) framework
- [allure](https://docs.qameta.io/allure/) reporting
- [travis](https://travis-ci.org/) CI

### Development
- [mypy](http://mypy.readthedocs.io/en/latest) static type checker tool
- [black](https://black.readthedocs.io/en/stable/) code formatter tool
- [flake8](http://flake8.pycqa.org/en/latest/) code style tool

> In addition a source code is **fully** [type annotated](https://docs.python.org/3/library/typing.html) ⭐

## Usage
![Usage](media/usage.gif)

### Quick start
From the root directory of your shell run following command:

```bash
./run-tests.sh help

Tool allows to simplify run of automated tests for POM sample project.

Available actions:
 - smoke                 run automated smoke tests
 - unittest              run automated unittest tests
 - all                   run all automated tests
 - help                  display help

Note:            help will be provided in case of no input parameters
```

### Tests (html) report sample
Run a bunch of tests (e.g smoke) via following command:
```bash
./run-tests.sh smoke
```

Then please open `test-report.html` file to see detailed testing report e.g:

![Screenshot](demoauto/image/report.png)

### Generate allure report
Please follow next instruction to generate allure report (mac OS example):
1. Update java via `brew cask install adoptopenjdk`
2. Install allure via `brew install allure`
3. Generate allure project via `allure serve report`

![Screenshot](demoauto/image/allure.png)

## Development notes

### Release History

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta
Author – _Volodymyr Yahello_.

Distributed under the `GPL v3` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request
