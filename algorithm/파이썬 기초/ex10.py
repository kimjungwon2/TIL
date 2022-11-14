from itertools import permutations

a = [1,2,3,4,5]

a = list(map(''.join,list(permutations(map(str,a),2))))

print(a)