clacule = 5/2
calculeInitial = clacule
calculeInt = int (clacule)
calculeFloat = float(clacule)
print("le resultat du calcule est :", calculeInitial) # valeur initial du calcule
print("le resultat du calcule est :", calculeInt) # valeur du calcule apres le cast en int
print("le resultat du calcule est :", calculeFloat) # valeur du calcule apres le cast en float

# en generale il est toujour preferable de castre des le calcule de l/operation pour eviter les resultat inattendu
calcule = float(5/2)
print("le resultat est :", calcule)

calcule2 = 5%2
calcule2 = int(calcule2)
print("le reste de la division (le modulo) est : ",calcule2)

calcule3 = 5+4*5
print("le resltat du calcule est : ", calcule3) # la re calcule par defaut comme en mathematique utilise BODMAS

print("Bonjour")
niveauJouer = int(input("entrez le niveau du jouer :"))
print("Bravo tu passe au niveau supperieur !")
niveauJouer +=1
print("Tu est au niveau : ", niveauJouer)