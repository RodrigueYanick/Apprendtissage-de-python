# En python les variables sont typee(ne contient pas de type predefinie au depart)

agePersone = 14
agepersonne2 = "14"

print(type(agePersone))
print(type(agepersonne2))

prixHt = 120.5
continuerPartie = True

print(type(prixHt))
print(type(continuerPartie))

print(agePersone)
print(agepersonne2)
print(prixHt)
print(continuerPartie)

print("age de la personne : ",agePersone)
print("age en string de la personne : ",agepersonne2)
print("prixht de la personne : ",prixHt)
print("es au'on continue la partie ? ",continuerPartie)

# utilisont les fonction format

texte = "l'age de la personne est {} et le prix hors taxe est {} euros"
print(texte.format(agePersone, prixHt))


# nous commencons avec les lecture dans le terminal
nomJouer = input("entrere le nom du jouer : ")
print ("le nom du jouer est :", nomJouer)

prixHt2 = input("entrez le prix hors taxe : ")

# la on a ete oblige de faire un cast pour pouvoir manipuler le prixHt2 car lors que on fait un input, l'element recuperer est debase une chane de caractere donc un cat etait necessaire
prixHt2 = int(prixHt2)
prixTTC = prixHt2 + (prixHt2 *20/100)
print ("le prix ttc est : ", prixTTC)