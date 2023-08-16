N = int(input())
A = list(map(int, input().split()))
visited = [False]*N
max_value = 1e-9

def max_v(lst):
    global max_value
    
    if(len(lst)==N):
        total = 0

        for i in range(N-1):
            total+= abs(lst[i]-lst[i+1])

        max_value = max(max_value,total)

        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            lst.append(A[i])

            max_v(lst)

            visited[i]=False
            lst.pop()

max_v([])
print(max_value)
