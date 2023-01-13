from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    input_country = (By.XPATH, "//input[@id='country']")
    check_box = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")
    purchase_text = (By.XPATH, "//strong[normalize-space()='Success!']")

    def get_input_country(self, text):
        return self.driver.find_element(*PurchasePage.input_country).send_keys(text)

    def set_country(self, text):
        return self.driver.find_element(By.LINK_TEXT, text).click()

    def get_check_box(self):
        return self.driver.find_element(*PurchasePage.check_box).click()

    def get_purchase_button(self):
        return self.driver.find_element(*PurchasePage.purchase_button).click()

    def get_purchase_text(self):
        return self.driver.find_element(*PurchasePage.purchase_text).text