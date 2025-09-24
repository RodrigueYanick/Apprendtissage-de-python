fic = open("mon_fichier.txt", "w")
# print(fic.read())

# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readlines()
# print(line)

numbre = 15
fic.write(str(numbre))
fic.write("Tigre\n")
fic.write("Hyene\n")
fic.write("porc")

fic.close()