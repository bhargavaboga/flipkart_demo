import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup_login(request):
    driver = webdriver.Edge()
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()