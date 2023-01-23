import time

import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_home_page(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info("Entering name as " + getData[0]["name"])
        home_page.get_name(getData[0]["name"])
        log.info("Entering email as " + getData[0]["email"])
        home_page.get_email(getData[0]["email"])
        log.info("Entering password as " + getData[0]["password"])
        home_page.get_password(getData[0]["password"])
        home_page.get_check()
        log.info("Setting gender as " + getData[0]["gender"])
        home_page.get_gender(getData[0]["gender"])
        home_page.get_status()
        home_page.get_submit()
        alert_massage = home_page.get_message()
        log.info("Text received in app is " + alert_massage)

        assert "Success!" in alert_massage
        self.driver.refresh()

    # @pytest.fixture(params=HomePageData.home_page_data)    # get data by input dictionary, but you need delete [0] in test_home_page
    @pytest.fixture(params=[HomePageData.getTestData("Test_Case_1"),
                            HomePageData.getTestData("Test_Case_2"),
                            HomePageData.getTestData("Test_Case_3")])   # get data from excel be test case name
    def getData(self, request):
        return request.param