import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.Moat_HomePage import MoatHomepage
from Pages.BasePage import BasePage
from Pages.Moat_Search_Page import SearchResultsPage
from Tests.configtest import init_driver

"""This test class is used to test the Search results page methods"""
@pytest.mark.usefixtures("init_driver")
class Test_SearchResultsPage():

    """ This Method is used to test whether the creative counts display are matching with  search results counts"""
    """ This method reads different search terms and validate the respective counts on each search term"""
    #@pytest.mark.skip(reason="Not testing this")
    def test_Verify_CreativeCount_Matches_SearchResults(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        for i in TestData.SearchTextList:
            rslttext = SearchResultsPage.Verify_CreativeCount_Matches_SearchResults(self.MoatSearchRslts,i)
            assert rslttext == "creatives count and  search results are matched"
            print(rslttext)
    """ This Method is used to test whether the creative counts display are matching with  search results counts for the term Saturn"""
    @pytest.mark.skip(reason="Not testing this")
    def test_Verify_CreativeCount_Matches_SearchResults_Saturn(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        rslttext = SearchResultsPage.Verify_CreativeCount_Matches_SearchResults(self.MoatSearchRslts,TestData.SearchSaturn)
        assert rslttext == "creatives count and  search results are matched"
        print(rslttext)

    """ This Method is used to test whether the creative counts display are matching with  search results counts for the term Saturday's Market"""
    @pytest.mark.skip(reason="Not testing this")
    def test_Verify_CreativeCount_Matches_SearchResults_SaturdayMarket(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        rslttext = SearchResultsPage.Verify_CreativeCount_Matches_SearchResults(self.MoatSearchRslts,TestData.SearchSaturdayMarker)
        assert rslttext == "creatives count and  search results are matched"
        print(rslttext)

    """ This Method is used to test whether the creative counts display are matching with  search results counts for the term Krux"""
    @pytest.mark.skip(reason="Not testing this")
    def test_Verify_CreativeCount_Matches_SearchResults_Krux(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        rslttext = SearchResultsPage.Verify_CreativeCount_Matches_SearchResults(self.MoatSearchRslts,TestData.SearchKrux)
        assert rslttext == "creatives count and  search results are matched"
        print(rslttext)

    """ This Method is used to test whether  the random links clciks giving different random search results """
    def test_Verify_randomlink_results(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        rslttext = SearchResultsPage.Verify_random_link_display_randomresults(self.MoatSearchRslts,TestData.SearchKrux,TestData.NoofIteratons)
        assert rslttext == "Random Results"
        print(rslttext)
    """ This Method is used to verify the Share ad button is present in all Ad search results when the mouse hover on ad page"""
    def test_Verify_sharelink_in_results(self):
        self.MoatSearchRslts = SearchResultsPage(self.driver)
        rslttext = SearchResultsPage.Verify_Sharelink_exists_in_dispResults_imgs(self.MoatSearchRslts,TestData.SearchSaturdayMarker)
        assert rslttext == "Share link is available for all search results"
        print(rslttext)