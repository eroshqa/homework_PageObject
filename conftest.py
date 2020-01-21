import pytest
from selenium import webdriver

#Параметры выбора браузера и языка пользователя
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

#Фикстура проверки введеного параметра языка пользователя
#@pytest.fixture
#def browser_language(request):
#    browser_language = request.config.getoption("language")
#    if browser_language == "":
#       raise pytest.UsageError("print --languge param")
#   return browser_language

#Фикстура запуска браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        user_language = request.config.getoption("language").lower()
        print(user_language)
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()