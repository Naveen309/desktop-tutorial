from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
@pytest.fixture()
def setup():
    service_obj = Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service = service_obj)
    return driver