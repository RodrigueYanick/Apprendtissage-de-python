ageUtilisateur = input("Entrez votre age")
try:
    ageUtilisateur = int(ageUtilisateur)
except ValueError:
    print("le format de l'age est invalide")
else:
    print("Tu as ",ageUtilisateur, "ans")
finally:
    print("FIN DU PROGRAMME...")