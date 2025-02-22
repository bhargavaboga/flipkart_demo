from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.basedriver import BaseDriver


class MobilesProductPage(BaseDriver):

    MOBILES_PRD_PG_TITLE_LOC = "._0FYq1K"
    APPLE_FILTER_CHECKBOX = "div[title='Apple']"
    APPLE_FILTER_APPLIED_ICON = ".nvQqOr .YcSYyC:first-child"

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    def get_mobiles_prd_pg_title_loc(self):
        return self.MOBILES_PRD_PG_TITLE_LOC

    def get_apple_filter_checkbox(self):
        # return self.APPLE_FILTER_CHECKBOX
        return self.driver.find_element(By.CSS_SELECTOR, self.APPLE_FILTER_CHECKBOX)

    def get_apple_filter_applied_icon(self):
        return self.APPLE_FILTER_APPLIED_ICON

    def wait_for_title_to_be_visible_and_return_loc(self):

        wait = WebDriverWait(self.driver,10)
        return self.wait_until_located_element_is_visible(By.CSS_SELECTOR,self.get_mobiles_prd_pg_title_loc())
        # return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.get_mobiles_prd_pg_title_loc())))

    def select_apple_filter_checkbox(self):
        # self.driver.find_element(By.CSS_SELECTOR,self.get_apple_filter_checkbox()).click()
        self.get_apple_filter_checkbox().click()
        # wait = WebDriverWait(self.driver,10)
        return self.wait_until_located_element_is_visible(By.CSS_SELECTOR,self.get_apple_filter_applied_icon())
        # return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.get_apple_filter_applied_icon())))
