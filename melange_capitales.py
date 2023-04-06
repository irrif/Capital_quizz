from random import choice


def melange_europe(capitales_europe):
    with open(capitales_europe, encoding="UTF-8") as capitales_europe_file:
        file = capitales_europe_file.readlines()

    file = [duo.split(":") for duo in file]
    country = [duo[0].strip(" ") for duo in file]
    capitales = [duo[1].strip(" ").rstrip("\n") for duo in file]
    dico = {country[x]: capitales[x] for x in range(len(country))}
    max_score = len(capitales)
    tries = 4
    score = 0

    while len(country) > 0 and tries > 0:
        choix_pays = choice(country)
        country.remove(choix_pays)
        print(choix_pays)
        reponse = input("Réponse : ")
        if reponse.lower() == dico.get(choix_pays).lower():
            score += 1
            print("Score :", score, "/", max_score)
        else:
            tries -= 1
            print("Mauvaise réponse, essais restants :", tries+1)
            reponse = input("Nouvelle réponse : ")
            if reponse.lower() != dico.get(choix_pays).lower() and tries > 0:
                while reponse.lower() != dico.get(choix_pays).lower() and tries > 0:
                    tries -= 1
                    print("Mauvaise réponse, essais restants :", tries+1)
                    reponse = input("Nouvelle réponse : ")
            else:
                score += 1
                print("Score :", score, "/", max_score)


melange_europe(capitales_europe="Capitales_Europe.txt")

