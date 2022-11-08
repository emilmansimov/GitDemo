from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome" #chrome
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://trade.thinkorswim.com/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(params=[{"username": "Emanmanem251", "password": "Manememan251"},#]}
                        {"username": "Emanom222", "password": "Manumemon231"}])

def data_load(request):
    return request.param

# C:\Users\Emil\Downloads\chromedriver_win32


