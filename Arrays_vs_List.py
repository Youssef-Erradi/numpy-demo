# encoding:utf-8
import numpy as np
import time
from sys import getsizeof

print("#Complexité en espace :")
n_elements = 10**6
x_list = []
x_list = [x for x in range(n_elements)]
x_np = np.array(x_list)
print(f"len(x_np) = {len(x_np)} et len(x_list) = {len(x_list)}")
print(f"taille de x_list en mémoire est {getsizeof(x_list)} octets")
print(f"taille de x_np en mémoire est {getsizeof(x_np)} octets")

print("- - - - -")

print("#Complexité en temps:")
start = time.process_time()
x_100_added = [x + 100 for x in x_list]
non_numpy_time = time.process_time() - start
print(x_100_added[-5:])
print(f"incrementer les valeurs d'une liste de {n_elements} élements est {non_numpy_time} secondes ")

start = time.process_time()
x_numpy = np.array(x_list)
x_np_100_added = x_numpy + 100
numpy_time = time.process_time() - start
print(x_np_100_added[-5:])
print(f"incrementer les valeurs d'un tableau numpy de {n_elements} élements est {numpy_time} secondes ")
