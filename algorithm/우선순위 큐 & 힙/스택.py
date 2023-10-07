from collections import deque

dq = deque()

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

dq.append(1)
dq.append(2)
dq.append(3)

stack.pop(-1)

print(stack)
