import sys
from collections import Counter
input = sys.stdin.readline

n= input().strip()

alpha = []

for i in n:
    alpha.append(i.upper())

data = Counter(alpha)

max_value = max(data.values())

count = 0 
answer =''
for i in data:
    if(data[i]==max_value):
        answer = i
        count+=1

if(count>=2):
    print('?')
else:
    print(answer)