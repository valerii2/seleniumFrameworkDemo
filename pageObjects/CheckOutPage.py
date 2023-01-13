from selenium.webdriver.common.by import By

from pageObjects.PurchasePage import PurchasePage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    check_out_button = (By.XPATH, "//button[normalize-space()='Checkout']")

    def get_check_out_button(self):
        self.driver.find_element(*CheckOutPage.check_out_button).click()
        purchasePage = PurchasePage(self.driver)
        return purchasePage
