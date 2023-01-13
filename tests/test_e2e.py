from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        products_page = home_page.get_shop()
        log.info("getting all products list")
        products = products_page.get_products_list()
        for product in products:
             product_name = product.find_element(By.XPATH, "div/h4/a").text
             if product_name == "Blackberry":
                 product.find_element(By.XPATH, "div/button").click()

        checkout_page = products_page.get_check_out_page()
        purchase_page = checkout_page.get_check_out_button()
        log.info("Entering country name")
        purchase_page.get_input_country("aus")
        self.wait_for_country_text("Austria")
        purchase_page.set_country("Austria")
        purchase_page.get_check_box()
        purchase_page.get_purchase_button()
        purchase_text = purchase_page.get_purchase_text()
        log.info("Text received in app is " + purchase_text)

        assert "Success!" in purchase_text


