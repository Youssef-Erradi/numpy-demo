#encoding:utf-8
# pour installer numpy : pip install numpy
import numpy as np

a = np.array([[1,2,3], [4,5,6] , [7,8,9], [10,11,12]])
print(a)
#Quelques informations sur un tableau NumPy
# La forme du tableau ex (3x3) ou (4x2x2)
print('shape :',a.shape)
# Nombre d'éléments dans le tableau.
print('len :',len(a))
# Nombre de dimensions du tableau.
print('ndim :',a.ndim)
# Le nombre total de valeurs contenues dans le tableau.
print('size :',a.size)
#Le type du tableau
print('dtype :',a.dtype)
print("- - -")

print("Un tableau de 4 lignes et 4 colones remplie avec 0.3")
b = np.full((4,4), .3)
print(b)
print("- - - - -\n")

print("Un tableau de 2-D de uns de 2 lignes et 3 colones")
c = np.ones((2,3))
print(c)
print("- - - - -\n")


print("Un tableau des zeros (4 lignes, 5colonnes )")
d = np.zeros((4,5),dtype='int')
print(d)
print("- - - - -\n")

print("Un tableau de nombres compris entre 10 et 20")
e = np.arange(10,21)
print(e)
print("- - - - -\n")

print("Matrice identité d'ordre 3")
i3 = np.eye(3)
print(i3)
print("- - - - -\n")

print("Vue d'un tableau numpy")
a_view = a.view()
a_view[0] = 88
print("a: ",a)
print("a_view : ",a_view)
print("id(a) = ",id(a))
print("id(a_view) = ",id(a_view))
print("- - - - -\n")

print("Copie d'un tableau numpy")
b_copy = b.copy()
b_copy[0] = 57
print("b: ",b)
print("b_copy : ",b_copy)
print("id(b) = ",id(b))
print("id(b_copy) = ",id(b_copy))
print("- - - - -\n")




