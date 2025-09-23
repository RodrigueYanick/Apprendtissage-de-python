compteur = 0

while compteur<=5:
    print ("je fait mon tour numero :", compteur)
    compteur += 1
print("le compteur est deja arriver a 5")

jeu_lancer = True
print("")

while jeu_lancer:
    choixMenu = input("> ")
    if choixMenu == "again":
        continue
    elif choixMenu == "quit":
        break
    elif choixMenu == "hello":
        print("Bonjour :) !")
    else:
        print("commande introuvable")

sentence = "bonjour tout le monde \nJe suis rodrigue"
for letter in sentence:
    print(letter)