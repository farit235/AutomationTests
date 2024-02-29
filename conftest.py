import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.binary_location = "/usr/bin/firefox"


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                               options=options)
    yield driver
    driver.quit()
