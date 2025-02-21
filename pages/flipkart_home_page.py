from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class FlipkartHomePage:

    ELECTRONICS_ICON = "div[aria-label='Electronics']"
    ELECTRONICS_CONTAINER = "._1UgUYI._2eN8ye"

    def __init__(self,driver):
        self.driver = driver

    def get_electronics_icon(self):
        return self.ELECTRONICS_ICON

    def get_electronics_container(self):
        return self.ELECTRONICS_CONTAINER

    def hover_on_electrnoics(self):

        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.get_electronics_icon()))
        actions.perform()

    def wait_and_return_electronics_container_locator(self):

        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.get_electronics_container())))


