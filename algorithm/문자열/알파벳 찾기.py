S = input()

data = dict()

for i,alpha in enumerate(S):
    if alpha not in data:
        data[alpha]=i

for i in range(ord('a'),ord('z')+1):
    if chr(i) in data:
        print(data[chr(i)],end=' ')
    else:
        print(-1, end=' ')