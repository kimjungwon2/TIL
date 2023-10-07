import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())


arr = [0 for _ in range(10)]

D = str(A*B*C)


for s in D:
    arr[int(s)] += 1

for i in range(10):
    print(arr[i])