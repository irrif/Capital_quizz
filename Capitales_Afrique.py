def capitale_afrique():
    from random import choice
    import time

    # Ouvre le fichier contenant les pays et capitales d'Afrique

    fichier = open("Capitales_Afrique.txt", "r", encoding="Utf-8")
    liste = fichier.readlines()
    fichier.close()

    liste1 = []
    liste_pays = []
    dico = {}
    for texte in liste:
        liste1.append(texte.split(":"))

    # Parcours les duo "Pays, Capitale" de la liste pour les mettre dans un dictionnaire avec en clé le pays et en
    # valeur la capitale

    for duo in liste1:
        pays = ""
        capitales = ""
        pays += duo[0]
        liste_pays.append(duo[0])
        capitales += duo[1]
        capitales = capitales.rstrip("\n")
        capitales = capitales.lstrip(" ")
        dico[pays] = capitales

    jouer = True
    chances = 5
    score = 0
    t0 = time.time()

    while jouer and chances > 1:
        if len(liste_pays) > 0:
            a = choice(liste_pays)
            print("Quelle est la capitale de :", a)
            liste_pays.remove(a)
            reponse = input("Réponse : ")
            if reponse.lower() == dico.get(a).lower():
                score += 1
                print("Score :", score, "/", 56)
            else:
                chances -= 1
                print("Mauvaise réponse, essais restants :", chances)
                reponse = input("Nouvelle réponse : ")
                if reponse.lower() != dico.get(a).lower() and chances > 1:
                    while reponse.lower() != dico.get(a).lower() and chances > 1:
                        chances -= 1
                        print("Mauvaise réponse, essais restants :", chances)
                        reponse = input("Nouvelle réponse : ")
                        if reponse.lower() == dico.get(a).lower():
                            score += 1
                            print("Score :", score, "/", 56)
                elif reponse.lower() == dico.get(a).lower():
                    score += 1
                    print("Score :", score, "/", 56)
        elif len(liste_pays) == 0:
            temps = (time.time() - t0).__round__(3)
            print("Vous avez mis", temps, "secondes pour finir")
            break
