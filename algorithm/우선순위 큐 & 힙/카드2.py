from collections import deque

dq = deque()
N = int(input())

for i in range(1,N+1):
    dq.append(i)

while len(dq) >1:
    dq.appendleft()
    dq.append(dq.popleft())
    