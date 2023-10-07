from itertools import permutations, combinations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

result = list(combinations(data, 2))
print(result)
