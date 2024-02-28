from selenium import webdriver

# Chemin vers le driver Selenium pour Chrome
chrome_driver_path = "/Users/omaimachefiai/industrialisation/env/lib/python3.11/site-packages"

# Initialisation du navigateur Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Ouvrir le site d'actualités/de commerce
driver.get("https://www.amazon.fr")

# Effectuer une recherche si nécessaire
# Exemple : Recherchez des articles liés à un certain sujet
search_box = driver.find_element_by_id("nav-search-submit-button")
search_box.send_keys("books")
search_box.submit()

# Collecter des informations sur les articles visibles
articles = driver.find_elements_by_xpath(
    "//div[@class='s-desktop-width-max s-desktop-content s-opposite-dir s-wide-grid-style sg-row']"
)

# Parcourir chaque article et collecter les informations nécessaires
for article in articles:
    # Titre de l'article
    title = article.find_element_by_xpath(".//h2[@class='a-size-base-plus a-color-base a-text-normal']").text

    # URL de l'article
    url = article.find_element_by_xpath(".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").get_attribute(
        "href"
    )

    # Afficher les informations dans la console
    print("Titre:", title)
    print("URL:", url)
    print("=" * 50)

# Fermer le navigateur
driver.quit()
