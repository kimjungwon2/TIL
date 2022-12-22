import math


def solution(denum1, num1, denum2, num2):

    answer = []

    y = denum1*num2 + denum2*num1
    x = num1 * num2

    z = math.gcd(x, y)

    answer.append(y//z)
    answer.append(x//z)

    return answer
