import Les_Fonctions
import math #(from math import sqrt ou encore * pour tout importer)
coucou = lambda:print("Bonjour chef")

coucou()

ttc = lambda prixHT:prixHT + (prixHT*20/100)

print(ttc(24000))

calculer = lambda a, b:a+b
print(calculer(10, 820))

resultat = math.sqrt(100)
print (resultat)

sinus = math.sin(42)
print(sinus)

def parler(personnage, message):
    print("{} - {}".format(personnage, message))

Les_Fonctions.dire("Rodrigue", "tu es beau")