N = int(input())
arr = list(map(int,input().split()))

answer = 0
visited = [False]*N

def max_value(list):
    global answer

    # 0~N-1 abs 합구하기
    if len(list) == N:
        total = 0 
        for i in range(N-1):
            total+=abs(list[i]-list[i+1])

        answer = max(answer,total)
        
        return 

    #재귀함수
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            list.append(arr[i])
            max_value(list)
            visited[i]=False
            list.pop()

max_value([])
print(answer)