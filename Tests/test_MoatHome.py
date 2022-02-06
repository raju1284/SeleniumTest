import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.Moat_HomePage import MoatHomepage
from Pages.BasePage import BasePage
from Tests.configtest import init_driver

""" This is test class to test the Moat Home page methods"""
@pytest.mark.usefixtures("init_driver")
class Test_MoatHome():
    """ This Method is to test Verify the Autocompleted text when the user enter the text in search box"""
    def test_verifyautocompletetext(self):
        self.MoatHomepage = MoatHomepage(self.driver)
        flag = MoatHomepage.Verify_Seacrh_Bar_autocomplete(self.MoatHomepage,TestData.SearchText)
        assert flag == "Typed search Text are matching with Autocomplete drop down values"



