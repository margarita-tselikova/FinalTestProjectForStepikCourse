from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Specify language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption('language')
    print(browser_language)
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
