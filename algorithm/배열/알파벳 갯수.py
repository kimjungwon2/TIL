import sys

input = sys.stdin.readline

stri = input().rstrip()
count = [0 for _ in range(26)]
alpha = dict()

for i in range(26):
    alpha[chr(97+i)] = i


for i in stri:
    count[alpha[i]] += 1

s = map(str,count)

print(' '.join(s))
