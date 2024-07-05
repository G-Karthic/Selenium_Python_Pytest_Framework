import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_obj = Service("C:/Users/Karthic/Documents/geckodriver-v0.33.0-win32")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "chrome":
        driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

