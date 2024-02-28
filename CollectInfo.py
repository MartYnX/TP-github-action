from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get(
    "https://www.amazon.fr/s?k=books&__mk_fr_FR=ÅMÅŽÕÑ&crid=PERU3TOCZEPS&sprefix=books%2Caps%2C101&ref=nb_sb_noss_1"
)
element = browser.find_element(By.ID, "nav-search-submit-button")
element.send_keys("books")
print(element)
time.sleep(3)
browser.close()