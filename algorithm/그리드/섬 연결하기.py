def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def compareParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False

def solution(n, costs):
    answer = 0
    count = 0
    
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    
    costs.sort(key = lambda x: x[2])

    for x in costs:
        if not compareParent(parent,x[0], x[1]):
            answer += x[2]
            unionParent(parent, x[0],x[1])
            count += 1

        if count == n - 1:
            break

    return answer