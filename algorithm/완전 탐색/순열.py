from itertools import permutations
from itertools import product

lista = [2, 3, 4, 5, 6]

for i,j in enumerate(lista):
    lista[i]=str(j)


a = list(map(''.join,permutations(lista, 3)))
b = list(map(''.join, product(lista, repeat=3)))
print(a)
print(b)
