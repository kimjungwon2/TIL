import sys 
from collections import Counter

input = sys.stdin.readline

N = int(input())

dice = [list(map(int,input().split())) for _ in range(N)]


arr =[]

for i in dice:
    a = Counter(i)
    length = len(a)
    same = False
    price = 0

    for k in a:
        if(length == 1):
            arr.append(50000+k*5000)
            break
        elif(length==2 and a[k]==3):
            arr.append(10000+k*1000)
            break
        elif (length == 2 and a[k] == 2 and same==False):
            same=True
            price+=2000+500*k
        elif(same==True):
            price+=500*k
            arr.append(price)
            same=False
        elif (a[k] == 2 and length == 3):
            arr.append(1000+100*k)
        elif(length==4):
            arr.append(max(a)*100)
            break

print(max(arr))

