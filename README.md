# Page object design pattern implementation in python
Represent most popular OOD pattern for Web UI automation using python programming language.

## Run automated tests
From the root directory of your shell run next command
- Smoke tests
```bash
~ ./run-tests smoke
```
- Unittest tests
```bash
~ ./run-tests unittest
```
- All tests
```bash
~ ./run-tests all
```

### Tests report sample
```bash
cachedir: .pytest_cache
Project: Pytest Page Object Model
Written by: Volodymyr Yahello
collected 14 items                                                                                                                                                                                               

tests/coverage/functional/pages/test_home_page.py::test_home_page_logo PASSED                                                                                                                              [  7%]
tests/coverage/functional/pages/test_home_page.py::test_home_page_contact PASSED                                                                                                                           [ 14%]
tests/coverage/functional/pages/test_home_page.py::test_home_page_sign_on PASSED                                                                                                                           [ 21%]
tests/coverage/functional/pages/test_home_page.py::test_home_page_support PASSED                                                                                                                           [ 28%]
tests/coverage/functional/pages/test_home_page.py::test_home_page_register PASSED                                                                                                                          [ 35%]
tests/coverage/functional/pages/test_register_page.py::test_register_page_register_text PASSED                                                                                                             [ 42%]
tests/coverage/functional/pages/test_register_page.py::test_set_first_name PASSED                                                                                                                          [ 50%]
tests/coverage/functional/pages/test_register_page.py::test_registration PASSED                                                                                                                            [ 57%]
tests/coverage/unittests/browsers/test_browsers.py::test_browser_name[Safari] PASSED                                                                                                                       [ 64%]
tests/coverage/unittests/browsers/test_browsers.py::test_browser_name[Chrome] PASSED                                                                                                                       [ 71%]
tests/coverage/unittests/browsers/test_browsers.py::test_browser_error PASSED                                                                                                                              [ 78%]
tests/coverage/unittests/map/test_urls.py::test_home_url PASSED                                                                                                                                            [ 85%]
tests/coverage/unittests/map/test_urls.py::test_register_url PASSED                                                                                                                                        [ 92%]
tests/coverage/unittests/map/test_urls.py::test_sign_on_url PASSED                                                                                                                                         [100%]

=========================================================================================== 14 passed in 25.30 seconds ===========================================================================================
removing .pytest_cache testing trash
environment is cleared
```

## Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all required python packages