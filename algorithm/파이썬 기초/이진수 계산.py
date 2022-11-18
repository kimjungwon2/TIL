import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(str, input().split())) for _ in range(n)]

answer = []


for i in arr:
    ans = int(i[0], 2)+int(i[1], 2)
    answer.append(bin(ans)[2:])

for i in answer:
    print(i)
