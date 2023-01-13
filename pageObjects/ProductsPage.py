from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    products_list = (By.XPATH, "//div[@class='card h-100']")
    check_out_page = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_products_list(self):
        return self.driver.find_elements(*ProductsPage.products_list)

    def get_check_out_page(self):
        self.driver.find_element(*ProductsPage.check_out_page).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

