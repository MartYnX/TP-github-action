import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestWikipediaSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(
            "https://fr.wikipedia.org/w/index.php?search=ordi&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1"
        )
        time.sleep(3)

    def tearDown(self):
        self.browser.close()

    def test_search_results_exist(self):
        list_title = self.browser.find_elements(By.CLASS_NAME, "mw-search-result-heading")
        self.assertTrue(len(list_title) > 0, "No search results found")

    def test_search_result_format(self):
        list_title = self.browser.find_elements(By.CLASS_NAME, "mw-search-result-heading")
        for el in list_title:
            href = el.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
            title = el.find_element(By.CSS_SELECTOR, 'a').get_attribute("title")
            self.assertIsInstance(href, str, "Href should be a string")
            self.assertIsInstance(title, str, "Title should be a string")
            self.assertNotEqual(len(href), 0, "Href should not be empty")
            self.assertNotEqual(len(title), 0, "Title should not be empty")

if __name__ == "__main__":
    unittest.main()