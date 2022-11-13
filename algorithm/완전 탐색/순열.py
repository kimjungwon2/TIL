from itertools import permutations

lista = [2, 3, 4, 5, 6]

for i,j in enumerate(lista):
    lista[i]=str(j)


a = list(map(''.join,(permutations(lista, 3))))
print(a)
