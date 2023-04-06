from V1 import Capitales_Afrique, Capitales_Europe

print("Capitales de l'Afrique (1), Capitales de l'Europe (2), Toutes les capitales (3), Quitter (9)")
entrer = int(input("Numéro : "))
if entrer == 1:
    Capitales_Afrique.capitale_afrique()
elif entrer == 2:
    Capitales_Europe.capitale_europe()
elif entrer == 3:
    Capitales_Afrique.capitale_afrique()
    Capitales_Europe.capitale_europe()
else:
    pass
