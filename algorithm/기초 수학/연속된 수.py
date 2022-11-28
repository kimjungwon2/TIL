def solution(num, total):
    answer = []
    a = 0
    ans = 0

    for i in range(num):
        a += i

    ans = (total - a)//num

    for i in range(num):
        answer.append(ans)
        ans += 1

    answer.sort()

    return answer
