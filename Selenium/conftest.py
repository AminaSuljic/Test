import pytest 
from selenium import webdriver
from selenium.webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
import time

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    selenium_driver = webdriver.Chrome(service=service)
    yield selenium_driver
    time.sleep(5)
    selenium_driver.quit()

