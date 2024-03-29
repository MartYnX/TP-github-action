from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from fortostring import toString

browser = webdriver.Chrome()
browser.get(
    "https://fr.wikipedia.org/w/index.php?search=ordi&title=Sp%C3%A9cial:Recherche&profile=advanced&fulltext=1&ns0=1"
)

listTitle = browser.find_elements(By.CLASS_NAME,"mw-search-result-heading")

def toFormatAndPrint(href, title):
    return print({"href":href, "title":title })


for el in listTitle:
    print(toString(el.find_element(By.CSS_SELECTOR, 'a').get_attribute("title"), el.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")))

    
   
 
time.sleep(3)
browser.close()