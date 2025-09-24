ma_chaine = "Bonjour tout le monde !"
print(ma_chaine.upper())
print(ma_chaine.capitalize())
print(ma_chaine.lower())
print(ma_chaine.title())
print(ma_chaine.encode())

print(ma_chaine.center(100)) # cette function va tout simplement faire une taille de 100 caractere et placer le mot au milieu des 100 caractere


print(ma_chaine.find("tout"))

# la fonction strip() enleve des espace avant et apres un mot ou une phrase

print(ma_chaine.replace("o", "a"))

print(ma_chaine.split(" "))