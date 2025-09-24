dict = {1:23, "nom":"Bathelemie"}
print(dict["nom"])
dict["chien"] = "bath"
print(dict)
dict["chien"] = "Dave"
print(dict)

valeur_supprimer = dict.pop("chien") # pour la suppression
print(valeur_supprimer)
print(dict)

del dict[1]
print(dict)

if "chien" in dict:
    print("oui")
else:
    print("non")

for key in dict:
    print(key)

for key in dict.keys():
    print(key)

for key in dict.values():
    print(key)

for k, v in dict.items():
    print("Key : {} -> value : {}".format(k, v))


def monDictionaire(**parametter):
    print(parametter)

monDictionaire(nom = "Rodrigue", prenom = "perine")