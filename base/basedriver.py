from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC

class BaseDriver:

    def __init__(self,driver):
        self.driver = driver

    def wait_until_located_element_is_visible(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.visibility_of_element_located((locator_type,locator)))

    def move_to_element_cust(self,web_elem):
        actions = ActionChains(self.driver)
        actions.move_to_element(web_elem).perform()

    def actions_click(self):
        actions = ActionChains(self.driver)
        actions.click().perform()