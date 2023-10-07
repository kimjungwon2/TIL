import math


def solution(numbers):
    answer = 0
    arr = []
    visited = [False]*(len(numbers)+1)
    final = []

    for i in numbers:
        arr.append(i)

    recur(0, arr, visited, '', final)

    answer = len(set(final))

    return answer


def recur(num, arr, visited, result, final):
    length = len(arr)
    if (num == length):
        return

    for i in range(1, length+1):
        if visited[i] == False:
            visited[i] = True

            result += arr[i-1]

            #소수 확인
            a = isPrime(int(result))
            if (a == True):
                final.append(int(result))
            else:
                a = False

            recur(num+1, arr, visited, result, final)

            #다시 올라가기
            visited[i] = False
            #문자열 자르기
            result = result[:-1]


def isPrime(numbers):
    number = int(numbers)

    if (number <= 1):
        return False

    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True
