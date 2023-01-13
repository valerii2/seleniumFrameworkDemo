import time

import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_home_page(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info("Entering name as " + getData["name"])
        home_page.get_name(getData["name"])
        log.info("Entering email as " + getData["email"])
        home_page.get_email(getData["email"])
        log.info("Entering password as " + getData["password"])
        home_page.get_password(getData["password"])
        home_page.get_check()
        log.info("Setting gender as " + getData["gender"])
        home_page.get_gender(getData["gender"])
        home_page.get_status()
        home_page.get_submit()
        alert_massage = home_page.get_message()
        log.info("Text received in app is " + alert_massage)

        assert "Success!" in alert_massage
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.home_page_data)
    def getData(self, request):
        return request.param