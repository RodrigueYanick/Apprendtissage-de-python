identifiant = "Rodrigue24"
mot_de_pass = "yandzurod"


print("interface de connexion")

user_id = input("entrez l'identifiant du jouer :")
lettreHasard = "x"
if lettreHasard in identifiant:
    print("vous devez changer de d'identifiant")
else:
    print("Vous pouvez continuer avec le mot de passe")
password = input("entrz le mot de passe du jouer :")

if password == mot_de_pass and user_id == identifiant:
    print("Vous etes connecter !! \nBienvenue "+user_id)
else:
    print("mauvais mot de passe")


age = 10
if age >= 0 and age <12:
    print("tu vest un enfant")
elif age >= 12 and age <=18:
    print("Vous etes un adolescent")
elif age > 18 and age < 30:
    print("Vous etes un jeune adulte")
elif age >= 30 and age <=59:
    print("Vous etes un adulte")
elif age >= 60 and age <= 80:
    print("Vous etes un senior")
else:
    print("soit vous etes sage ou vous n'existez pas")