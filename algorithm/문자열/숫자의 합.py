import sys
input = sys.stdin.readline

N=int(input())
M=input()

sum_value=0

for i in range(N):
    sum_value+=int(M[i])

print(sum_value)

