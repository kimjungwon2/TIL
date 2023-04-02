ans = 0

def solution(k, dungeons):
    answer = 0
    length = len(dungeons)
    visited = [False] * length

    recur(k, dungeons, length, visited, answer)

    return ans

def recur(k, dungeons, length, visited, answer):
    global ans
    ans = max(ans, answer)

    min_value = dungeons[0][0]

    for i in dungeons:
        min_value = min(min_value,i[0])

    if(k<min_value):
        return

    for i in range(length):
        if(k>=dungeons[i][0] and visited[i]==False):
            visited[i]=True
            k-=dungeons[i][1]
            answer+=1

            recur(k, dungeons, length, visited, answer)

            #다시 위로 올라가기
            visited[i]=False
            k+=dungeons[i][1]
            answer-=1