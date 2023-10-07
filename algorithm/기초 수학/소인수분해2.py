import math


def solution(n):
    answer = []
    divisor = 2

    while (n >= 2):
        if (n % divisor == 0):
            if (answer.count(divisor) == 0):
                answer.append(divisor)
            n = n/divisor

        else:
            divisor += 1

    return answer
