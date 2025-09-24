def dir_bonjour():
    print ("bonjour tout le monde !")

dir_bonjour()

def dire(nom_personne, message_personne):
    print("{} : {}".format(nom_personne, message_personne))

dire("Rodrigue", "Bonjour a tous !")

def dir(nom_personne = "Tom", message_personne = "je suis un chat", age = 18):
    print("{} ({} ans) : {}".format(nom_personne, age, message_personne))

dir()

def show_inventory(*list_items):
    for item in list_items:
        print(item)

show_inventory("epee")
show_inventory("epee", "arc", "bouclier", "casque", "armure", "botte")

def le_plus_grand_nombre(nombre1, nombre2):
    if nombre1>nombre2:
        return nombre1
    elif nombre2>nombre1:
        return nombre2
    return "EGALITE"

print(le_plus_grand_nombre(15,20))