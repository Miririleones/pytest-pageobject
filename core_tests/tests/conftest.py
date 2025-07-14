import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# def pytest_addoption(parser): -- ПОДУМАТЬ КАК РАБОТАЕТ
#     parser.addoption('--language', action='store', default='en',
#                      help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    # language = request.config.getoption("language") -- ПОДУМАТЬ КАК РАБОТАЕТ
    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language}) -- ПОДУМАТЬ КАК РАБОТАЕТ
    options.add_argument('--headless')
    
    print("\n start browser for test..")
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\n quit browser..")
    browser.quit()