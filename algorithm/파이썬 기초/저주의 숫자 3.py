def solution(n):
    answer = 0

    for i in range(1, n+1):
        answer += 1

        while (True):
            if (answer % 3 != 0 and str(answer).find('3') == -1):
                break

            answer += 1

    return answer
