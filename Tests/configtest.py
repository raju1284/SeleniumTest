import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import TestData

""" This function is used for Initializing the Web driver"""
@pytest.fixture(params =["chrome"],scope = 'class')
def init_driver(request):
    if request.param == "chrome":
        ser = Service(TestData.chrom_driver_exe)
        driver = webdriver.Chrome(service=ser)
    if request.param == "ie":
        ser = Service(TestData.ie_driver_exe)
        driver = webdriver.Chrome(service=ser)
    request.cls.driver= driver
    driver.maximize_window()
    yield
    driver.close()


