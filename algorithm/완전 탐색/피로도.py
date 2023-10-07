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

    for i in range(length):
        if (k >= dungeons[i][0] and visited[i] == False):
            visited[i] = True

            recur(k-dungeons[i][1], dungeons, length, visited, answer+1)

            #다시 위로 올라가기
            visited[i] = False
