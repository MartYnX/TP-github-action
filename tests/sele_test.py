from fortostring import toString


def test_toString():
    # Entrées de test
    title = "Titre"
    href = "https://exemple.com/article"

    #Appel de la fonction à tester
    output = toString(title, href)
    print (output)
    # Assertion pour vérifier la sortie
    assert output == f"l'article intitule {title} a pour lien {href}"