from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.ProductsPage import ProductsPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # test_e2e data
    shop_link = (By.LINK_TEXT, "Shop")

    # test_homePage data
    name = (By.XPATH, "//input[@name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    status = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    message = (By.XPATH, "//strong[normalize-space()='Success!']")

    # test_e2e methods
    def get_shop(self):
        self.driver.find_element(*HomePage.shop_link).click()
        productsPage = ProductsPage(self.driver)
        return productsPage

    # test_HomePage methods
    def get_name(self, text):
        return self.driver.find_element(*HomePage.name).send_keys(text)

    def get_email(self, text):
        return self.driver.find_element(*HomePage.email).send_keys(text)

    def get_password(self, text):
        return self.driver.find_element(*HomePage.password).send_keys(text)

    def get_check(self):
        return self.driver.find_element(*HomePage.check).click()

    def get_gender(self, text):
        return Select(self.driver.find_element(*HomePage.gender)).select_by_visible_text(text)

    def get_status(self):
        return self.driver.find_element(*HomePage.status).click()

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit).click()

    def get_message(self):
        return self.driver.find_element(*HomePage.message).text
