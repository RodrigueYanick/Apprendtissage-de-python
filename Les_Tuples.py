mon_tuple = (45, 46)
print(type(mon_tuple))

print(mon_tuple[1], mon_tuple[0])

(nombre1, nombre2) = (24, 65)
print(nombre1)
print(nombre2)
nombre1 = 254
print(nombre1)


def get_player_possition():
    posX = 200
    posY = 250
    return (posX, posY)
cordX = 0
cordY = 0

print("la position du jouer est ({} - {})".format(cordX, cordY))

(cordX, cordY) = get_player_possition()

print("la position du jouer est ({} - {})".format(cordX, cordY))