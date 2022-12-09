# 덧셈의 약수들을 구한다.
# 완전 탐색으로 최적의

def solution(brown, yellow):
    answer = []
    a = brown + yellow
    b = []

    for i in range(1, a+1):
        if (a % i == 0):
            b.append(i)

    length = len(b)

    for i in range(length):
        for j in range(length):
            if (b[i] <= brown and b[i] >= b[j] and b[i]*b[j] == a and
               (b[i]-2)*(b[j]-2) == yellow):
                answer.append((b[i], b[j]))

    return answer[0]
