from collections import Counter


def solution(clothes):
    arr = []
    sum = 1

    for i in clothes:
        arr.append(i[1])

    counter = Counter(arr)

    for i in counter:
        sum *= (counter[i]+1)

    return sum-1
