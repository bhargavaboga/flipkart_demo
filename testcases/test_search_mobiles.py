from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest
import pytest
from pages.flipkart_home_page import FlipkartHomePage

@pytest.mark.usefixtures("setup_login")
class TestFlipkartMobiles(softest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.flipkart_home_page = FlipkartHomePage(self.driver)

    def test_search_i_phones_page_nav(self):

        self.soft_assert(self.assertEqual,self.driver.title,"Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!")

        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        self.flipkart_home_page.hover_on_electronics()
        self.soft_assert(self.assertNotEqual, self.flipkart_home_page.wait_and_return_electronics_container, False)
        mobiles_product_page = self.flipkart_home_page.open_mobiles_product_page()
        self.soft_assert(self.assertNotEqual,mobiles_product_page.wait_for_title_to_be_visible_and_return_loc(),False)

        filter_applied_apple = mobiles_product_page.select_apple_filter_checkbox()
        self.soft_assert(self.assertIn,"Apple",filter_applied_apple.text)

        filter_apple_phones_page5 = self.driver.find_element(By.XPATH,"//a[normalize-space()='5']")
        filter_apple_phones_page5.click()

        wait.until_not(EC.text_to_be_present_in_element_attribute((By.XPATH,"//a[normalize-space()='1']"),"class","A1msZJ"))
        wait.until(EC.text_to_be_present_in_element_attribute((By.XPATH,"//a[normalize-space()='5']"),"class","A1msZJ"))

        actions.scroll_to_element(self.driver.find_element(By.CSS_SELECTOR,"._1G0WLw>span:first-child")).perform()

        # assert "Page 5 of " in driver.find_element(By.CSS_SELECTOR, "._1G0WLw>span:first-child").text
        # st.assertEqual("Page 5 of ",driver.find_element(By.CSS_SELECTOR, "._1G0WLw>span:first-child").text)
        self.soft_assert(self.assertIn,"Page 5 of ",self.driver.find_element(By.CSS_SELECTOR, "._1G0WLw>span:first-child").text)

        self.assert_all()

        self.driver.save_screenshot("..\\Screenshots\\Filter_ApplePhones_Page5.png")

        # driver.close() # This is throwing ---- OSError: [WinError 6] The handle is invalid
        # self.driver.quit()

# fm = FlipkartMobiles()
# fm.test_search_i_phones()