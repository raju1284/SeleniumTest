from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
""" This Moat Home Page class defines Moat Home Page locators and specific test methods"""
class MoatHomepage(BasePage):

    """ Moat Home Page Web Locators"""
    AD_SEARCH_BAR = (By.XPATH, "//input[contains(@id,'adsearch-input')]")
    AD_SEARCH_DROPDOWN = (By.XPATH, "//div[contains(@id,'adsearch-dropdown')]")
    AD_SEARCH_DROPDWON_VALUES = (By.XPATH,"//div[contains(@id,'adsearch-dropdown')]/div/div")
    SEARCH_AUTOCOMPLETE_TEXT = (By.XPATH, "//div[@class='auto-complete-text']")
    """ Constructor Initialization"""
    """ Also Navigate to specified URL"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    """ This method is to check the enter text matching with  autocomplete text dropdown  values"""
    """ Enter at least two character in search box"""
    """ It will check the listed  autocomplete text down values with the entered search text of first two chars"""
    """ If any one of the auto complete text drop down values  except Brand text are not matched with first two chars then the this will fail"""

    def Verify_Seacrh_Bar_autocomplete(self, searchtext):
        print("\nEnter text in search box: "+ searchtext)
        print("Autocomplete Dropdown values text: ")
        if len(searchtext) > 1:
            self.do_send_keys(self.AD_SEARCH_BAR,searchtext)
            self.driver.implicitly_wait(5)

            srchdropdownelementslist = self.listoffindelements(str(self.AD_SEARCH_DROPDWON_VALUES[1]))
            cnt = 0

            if len(srchdropdownelementslist) > 0:
                for ele in srchdropdownelementslist:
                    if ele.text.find(searchtext[0:2]) == -1:
                        cnt = cnt + 1
                    print(ele.text)
            if cnt > 1:
                return "Typed search Text are not matching with Autocomplete drop down values"
            else:
                return "Typed search Text are matching with Autocomplete drop down values"
        else:
            return "Enter the text more than two characters"



