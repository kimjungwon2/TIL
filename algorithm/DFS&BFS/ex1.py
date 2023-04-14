answer = 0


def solution(numbers, target):

    length = len(numbers)

    recur(numbers, target, 0, 0, length)

    return answer


def recur(numbers, result, target, n, length):
    global answer
    if (length == n):
        if (result == target):
            answer += 1
            return
        else:
            return

    recur(numbers, result+numbers[n], target, n+1, length)
    recur(numbers, result-numbers[n], target, n+1, length)
