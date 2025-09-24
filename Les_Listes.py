import copy


inventory = list()
invent = []
invent1 = [2,3,4,5,"bonjour"]
invent2 = ["bomjour"]*10

invent3 = range(20)

i=0
while i <len(invent3):
    print(i)
    i+=1

print(invent2)

invent4 = ["rodrigue", "divine", "inona", "olivia"]
for value in invent4:
    print(value)

print(invent4[:])
print(invent4[2:])
print(invent4[1:])
print(invent4.count("divine"))

liste1 = ["nom", "prenom", "age", "sexe"]
liste2 = liste1

# sur cette exemple, nous pouvons clairement voir que une liste reste unique c-a-d compare au chaine de caractere que lorsque on effectue une modification sur une copie, les autres ne sont pas affecter, pour les listes c'est different une modification sur une copie moi=difie toutes les autres copie.
# en gros moi je pense que c'est parceque les listes et copies des listes on le meme emplacement en memoire 
print("liste 1 : ", liste1[:])
print("liste 2 : ", liste2[:])
liste2.append("niveau scolaire")
print("liste 1 : ", liste1[:])
print("liste 2 : ", liste2[:])

# une astuce pour arranger ce probleme est en utilisant la fonction deepcopy
liste3 = copy.deepcopy(liste1)

print("liste 1 : ", liste1[:])
print("liste 3 : ", liste3[:])
liste2.append("niveau scolaire")
print("liste 1 : ", liste1[:])
print("liste 3 : ", liste3[:])

# concatenetion d'une liste
liste4 = ["nom_pere", "nom_mere", "nom_chien"]

liste1.extend(liste4)
liste1 += liste4

print (liste1)

print("----------------------------------------------------------")
print(liste1)

for object in liste1:
    print(object)

# aide a connaitre l'indice des elements de la liste
for object in enumerate(liste1):
    print(object)


for indice_object, valeur_object in enumerate(liste1):
    print("element d'indice {} -> {}".format(indice_object, valeur_object))
