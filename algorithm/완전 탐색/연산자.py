from itertools import permutations
n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))
operator = '+' * op[0] + '-' * op[1] + '*' * op[2] + '/' * op[3]
operator_perm = permutations(operator, n-1)


print(list(operator_perm))