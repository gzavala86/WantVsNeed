from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
driver = webdriver.Chrome("C:\Python27\chromedriver.exe")
driver.get("https://wantvsneed.com")


class WantVSSearch(unittest.TestCase):

    def setup(self):
        self.driver = wbdriver.Chrome()
    def test_search_want_vs_need_newsletter(self):
        driver = self.driver
        driver.get("https://wantvsneed.com")
        self.assertIN("want", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("kimonos")
        elem.end_keys(Keys.Search)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
        


class WantVSNewsLetter(unittest.TestCase):

    def setup(self):
        self.driver = wbdriver.Chrome()
    def test_want_vs_need_newsletter(self):
        driver = self.driver
        driver.get("https://wantvsneed.com")
        driver.implicitly_wait(10)
        driver.find_element_by_id("cars").click()

        
