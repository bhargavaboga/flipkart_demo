from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest
import pytest
from pages.flipkart_home_page import FlipkartHomePage

class TestFlipkartMobiles(softest.TestCase):

    def test_search_i_phones_page_nav(self):

        self.soft_assert(self.assertEqual,self.driver.title,"Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!")

        wait = WebDriverWait(self.driver, 10)

        actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Electronics']"))
        # actions.perform()

        fp_h_p = FlipkartHomePage(self.driver)
        fp_h_p.hover_on_electrnoics()
        # self.soft_assert(self.assertNotEqual,wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"._1UgUYI._2eN8ye"))),False)
        self.soft_assert(self.assertNotEqual,fp_h_p.wait_and_return_electronics_container_locator, False)

        # driver.save_screenshot("..\\Screenshots\\Home_Page_Electronics.png")
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"a[aria-label='Mobiles']"))
        actions.perform()
        # driver.save_screenshot("..\\Screenshots\\Home_Page_Mobiles.png")
        actions.click()
        actions.perform()
        # driver.save_screenshot("..\\Screenshots\\Mobiles_Page.png")

        self.soft_assert(self.assertNotEqual,wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"._0FYq1K"))),False)

        self.driver.find_element(By.CSS_SELECTOR,"div[title='Apple']").click()
        filter_apple = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".nvQqOr .YcSYyC:first-child")))
        # print(filter_apple.text)
        # assert "Aple" in filter_apple.text
        self.soft_assert(self.assertIn,"Apple",filter_apple.text)

        # driver.save_screenshot("..\\Screenshots\\Filter_ApplePhones.png")

        # filter_apple_phones_page1 = driver.find_element(By.XPATH,"//a[normalize-space()='1']")
        # print(filter_apple_phones_page1.get_attribute("class"))

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