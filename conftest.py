import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



#def pytest_addoption(parser):
 #  parser.addoption('--language', action='store', default=None,
  #                  help="Choose language: en or es")
language = None

@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)


#def browser(request):
 #   browser = webdriver.Chrome()
  #  user_language = request.config.getoption("language")
   # yield browser
    #print("\nquit browser..")
    #browser.quit()