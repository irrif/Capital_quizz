import random
import time

# Lit le fichier et met les lignes dans une liste

with open("Capitales_Europe.txt", "r", encoding="Utf-8") as fichier:
    capitales_europes = fichier.readlines()

liste_pays = []
dico = {}
chances = 5
score = 0

# Extrait pays et capitales et les mets dans un dictionnaire

for duo in capitales_europes:
    duo = duo.rstrip("\n")
    duo = duo.split(":")
    duo[0] = duo[0].rstrip(" ")
    duo[1] = duo[1].lstrip(" ")
    liste_pays.append(duo[0])
    dico[duo[0]] = duo[1]

t0 = time.time()

while len(liste_pays) > 0 and chances > 0:
    print("--- STEP 0 ---")
    pays = random.choice(liste_pays)
    print("Quelle est la capitale de :", pays)
    liste_pays.remove(pays)
    reponse = input("Réponse : ")
    if reponse.lower() == dico.get(pays).lower():
        print("--- STEP 1 ---")
        score += 1
        print("Score :", score, "/", 48)
    else:
        print("--- STEP 2 ---")
        chances -= 1
        print("Mauvaise réponse, essais restant :", chances)
        reponse = input("Nouvelle réponse : ")
        if reponse.lower() != dico.get(pays).lower() and chances > 0:
            while reponse.lower() != dico.get(pays).lower() and chances > 0:
                print("--- STEP 3 ---")
                chances -= 1
                print("Mauvaise réponse, essais restant :", chances)
                reponse = input("Nouvelle réponse : ")

        else:
            score += 1
            print("Score :", score, "/", 48)
temps = time.time()-t0
print("Vous avez mis ", temps, "secondes pour finir")
