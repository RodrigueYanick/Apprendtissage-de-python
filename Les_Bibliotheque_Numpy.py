import numpy as np

a = np.array([1, 2, 3], dtype="float")
print(type(a[0]))
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(c)
print(b.ndim) # la dimension de b
print(c.size) # le nombre d'element dans le array
print(b.shape) # forme de l'array

# vecteur/ matrice rempli de 0
print(np.zeros((3, 2, 4), dtype="int"))

# vesteur/ matrice rempli de 1
print(np.ones((3, 2, 4), dtype="int"))
# Vecteur/ matrice rempli d'une autre valeur
print(np.full((3, 2, 4), 55))
# Matrice identiten
print(np.identity(5))
# Matrice a intervalle regulier constant
print(np.arange(3, 14, 0.2))
# matrice a intervalle regulier constant avec x size
print(np.linspace(3, 14, 9).reshape(3, 3))
# Nombre decimaux entre 0 et 1 uniform distribution
print(np.random.rand(4, 2))

# Nombres decimaux (Normal distribution) moyenne = 0 / variance = 1
print(np.random.randn(4, 2))
# Nombres d'entiers
print(np.random.randint(1, 101, size=(3,3)))

# Afficher certains elements
print(b[0, :]) # une seul ligne

print(b[0:2, :]) # recuperrer deux ligne

print (b[:, 0]) # la premiere column

print(b[:, 1:3]) # les deux derniere column

print(b[-1]) # la derniere column

# clule specifique 
print(b[2, 2]) # recuperrer une celule specifique 

file = np.random.randint(0, 101, size=(3, 10))
# Les filters
print(file)
print(file>90)
print(file[file>90])
file[(file>90) & (file%2 == 0)]
print(file[(file>90) & (file%2 == 0)])


# distinction entre view et copy
f = np.zeros((3, 2, 4))
# d = f.copy()[0:2, :, :]
d = f[0:2, :, :] 
print(d)

# modification sur la premier partie. la ont remplace tout les zero par 2 excepte les derniers column
d[0, :, :3] = 2
print(d)

# modifier les dernieres column des deux partie
d[:, :, -1] = [[9, 8], [7, 6]]
print(d)

# donner la valeur 3 a tout les 0
d[d==0]=3
print(d)


a = np.linspace(0, 10, 6).reshape(3, 2)
print(a)
a = a.transpose()
print(a)

bx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print(np.flip(bx)) # retourner la matrice au sens inverse

# Matrice retourner 2D (toutes les lignes + toutes les colonnes)
cx = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print(np.flip(cx, axis=0)) # au sense des lignes
print(np.flip(cx, axis=1)) # dans le sens de colonnes

# --------------------------------------------------------------------------
# Operations Mathematiques et statistiques

a = np.random.randint(1, 11, size=(3))
b = np.random.randint(1, 11, size=(3))
print("a vaut ",a)
print("b vaut ",b)
print ("a + b = ",a+b)
print ("a - b = ",a-b)
print ("a * b = ",a*b)
print ("a / b = ",a/b)

a = np.random.rand(3, 4)
print(a)
print(a.sum())
print(a.max())
print(a.min())
print(a.mean()) # moyenne
print(a.std()) # ecartype
print(a*2)


# La sauvegarde dans un fichier
import pandas as pd
# np.save("mon_fichier", a)
# np.savetxt("mon_fichier.csv", a)
# df = pd.DataFrame(a)
# df.to_csv("mon_fichier.csv", index=False)


# charger un fichier sur python
b = np.load("mon_fichier.npy")
print(b)

c = np.genfromtxt("mon_fichier.csv")
print(c)