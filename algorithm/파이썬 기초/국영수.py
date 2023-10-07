import sys
input = sys.stdin.readline

n = int(input())

arr = [list(input().split()) for _ in range(n)]

for i in arr:
    i[0]=str(i[0])
    i[1]=int(i[1])
    i[2]=int(i[2])
    i[3]=int(i[3])


arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for key in arr:
    print(key[0])
