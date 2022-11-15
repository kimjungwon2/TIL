import sys
from collections import Counter
input = sys.stdin.readline

N = input().strip()

alpha = []

string = ''

for index,i in enumerate(N):
    if (i == ' '):
        alpha.append(string)
        string=''
        continue
    string+=i.lower()

    if(index==len(N)-1):
        alpha.append(string)



data = Counter(alpha)
count = 0

for i in (data.keys()):
    count += data[i]

print(count)
