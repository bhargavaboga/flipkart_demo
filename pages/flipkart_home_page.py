from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.basedriver import BaseDriver
from pages.mobiles_product_page import MobilesProductPage


class FlipkartHomePage(BaseDriver):

    ELECTRONICS_ICON = "div[aria-label='Electronics']"
    ELECTRONICS_CONTAINER = "._1UgUYI._2eN8ye"
    MOBILES_ICON = "a[aria-label='Mobiles']"

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    def get_electronics_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.ELECTRONICS_ICON)

    def get_locator_electronics_container(self):
        return self.ELECTRONICS_CONTAINER

    def get_mobiles_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.MOBILES_ICON)

    def hover_on_electronics(self):
        self.move_to_element_cust(self.get_electronics_icon())

    def wait_and_return_electronics_container(self):
        return self.wait_until_located_element_is_visible(By.CSS_SELECTOR, self.get_locator_electronics_container())

    def open_mobiles_product_page(self):
        self.move_to_element_cust(self.get_mobiles_icon())
        self.actions_click()
        return MobilesProductPage(self.driver)
