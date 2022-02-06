import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.Moat_HomePage import MoatHomepage

""" This Moat Home Search reulst Page class defines Search Results Page locators and specific test methods"""
class SearchResultsPage(BasePage):
    """ Search Results Page Locators"""
    AUTOCOMPLETE_TEXT_ELE_FIRST = (By.XPATH, "//div[@class='auto-complete-text']")
    CREATIVES_COUNT_DISP = (By.XPATH, "//div[@class='creative-count']")
    ELE_LOAD_MORE = (By.XPATH,"//a[@class='er-load-more']")
    ELES_CREATIVE_DISP_RSLTS = (By.XPATH,"//div[@class='er-creatives']/div[@class='masonry-container show']/child::div[@class='er-creative-container']")
    ELES_CRE_COMB_DISP_RSLTS = (By.XPATH,"//div[@class='er-creatives']/div[@class='masonry-container show']/child::div[@class='er-combined-creatives']/div")
    ELE_CRE_COMB_DISP_RSLTS = (By.XPATH,"//div[@class='er-creatives']/div[@class='masonry-container show']/child::div[@class='er-combined-creatives']")
    ELE_HomePageLink = (By.XPATH, "//a[@href='/']")
    Results_section = (By.XPATH,"//div[@class='dotcom-creatives-container creatives-container']")
    ELE_Random_link = (By.XPATH, "//a[@href='/random_brand']")
    ELE_Random_Page_Text = (By.XPATH, "//div[@class='entity-label']/span[@class='page-type']")
    ELE_AD_Search_Result = (By.XPATH, "//a[@class='ca-digest-link pointer']")
    """Constructor Initialization"""
    """Also Navigate to specified URL"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)
    """This method will verify the creative counts display on the top of page with search results section"""
    """Need to pass the search text for validating creative counts"""
    """Also print the counts for verification"""
    """ If counts are not matched then this method will fail"""
    def Verify_CreativeCount_Matches_SearchResults(self,searchtext):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        self.do_send_keys(MoatHomepage.AD_SEARCH_BAR,searchtext)
        self.do_click(self.AUTOCOMPLETE_TEXT_ELE_FIRST)
        time.sleep(5)
        creativecnts_text = self.get_element_text(self.CREATIVES_COUNT_DISP)
        cnt = creativecnts_text.split(" ")
        cnt_disp = int(cnt[0])

        eleloadmore = self.findelement(str(self.ELE_LOAD_MORE[1]))
        while eleloadmore.is_displayed():
            eleloadmore.click()
            time.sleep(5)
        creativeelesdisp = self.listoffindelements(str(self.ELES_CREATIVE_DISP_RSLTS[1]))
        combinecreativelesdisp = self.listoffindelements(str(self.ELES_CRE_COMB_DISP_RSLTS[1]))
        cntofcreativesdisp = len(creativeelesdisp) + len(combinecreativelesdisp)
        self.do_click(self.ELE_HomePageLink)
        print("Disp_Creatives count :"+str(cnt_disp))
        print("Results_Creatives count :"+str(cntofcreativesdisp))
        if cnt_disp == cntofcreativesdisp:
            return "creatives count and  search results are matched"
        else:
            return "creatives count and  search results are  not matched"

    """This Method will verify when random link clicks  displays different results section each time"""
    """Need to pass the search text initially for going to random link displayed page"""
    """Also print the random search results for verification """
    def Verify_random_link_display_randomresults(self,searchtext,NoofIterartions):
        self.do_send_keys(MoatHomepage.AD_SEARCH_BAR, searchtext)
        self.do_click(self.AUTOCOMPLETE_TEXT_ELE_FIRST)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        elerandomlnk = self.findelement(str(self.ELE_Random_link[1]))
        pagetitle = []
        for i in range(0,NoofIterartions):
            if elerandomlnk.is_displayed():
                elerandomlnk.click()
                time.sleep(5)
            # driver.refresh()
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
            elerandomlnk = WebDriverWait(self.driver, 15, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.presence_of_element_located(self.ELE_Random_link))

            elepagetype = self.findelement(str(self.ELE_Random_Page_Text[1]))
            pagetitle.append(elepagetype.text)
        print("Random Search Results for five times:")
        print(pagetitle)
        if len(pagetitle) == len(set(pagetitle)):
            return "Random Results"
        else:
            return "Not Random Results"

    """This Method will verify the Share Ad link button present in each Ad Seach results when the mouse hover on ad page"""
    """If any one of the Ad page  results dont have Share link this method will fail"""
    def Verify_Sharelink_exists_in_dispResults_imgs(self,searchtext):
        self.do_send_keys(MoatHomepage.AD_SEARCH_BAR, searchtext)
        self.do_click(self.AUTOCOMPLETE_TEXT_ELE_FIRST)
        #WebDriverWait(self.driver, 10).until(
        #   lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        creativeelesdisp = self.listoffindelements(str(self.ELES_CREATIVE_DISP_RSLTS[1]))
        try:
            #elecombined = self.driver.find_element(By.XPATH, "//div[@class='er-creatives']/div[@class='masonry-container show']/child::div[@class='er-combined-creatives']")
            combinecreativelesdisp = self.listoffindelements(str(self.ELE_CRE_COMB_DISP_RSLTS[1]))
        except:
            combinecreativelesdisp = []


        a = ActionChains(self.driver)
        flag = 0
        for i in creativeelesdisp:
            a.move_to_element(i).perform()
            self.driver.implicitly_wait(2)
            if self.findelement(str(self.ELE_AD_Search_Result[1])).is_displayed():
                flag = flag + 1
        if len(combinecreativelesdisp) > 0:
            for i in combinecreativelesdisp:
                a.move_to_element(i).perform()
                self.driver.implicitly_wait(2)
                if self.findelement(str(self.ELE_AD_Search_Result[1])).is_displayed():
                    flag = flag + 1
        cntofcreativesdisp = len(creativeelesdisp) + len(combinecreativelesdisp)
        if flag == cntofcreativesdisp:
            return "Share link is available for all search results"
        else:
            return "Share link is not available for all search results"









