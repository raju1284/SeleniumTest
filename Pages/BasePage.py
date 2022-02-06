"""This is parent class for all  Pages"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData

class BasePage:
    """Constructor Initialization  """
    def __init__(self,driver):
        self.driver = driver
    """Generic methods for click,gettext,sendkeys  """
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    def get_title(self,title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    def close_browser(self):
        self.driver.close()
    def listoffindelements(self,by_xpath):
        elements = self.driver.find_elements_by_xpath(by_xpath)
        return elements
    def findelement(self,by_xpath):
        element = self.driver.find_element_by_xpath(by_xpath)
        return element








