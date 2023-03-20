from collections import Counter


def solution(nums):

    answer = 0

    length = len(nums)/2
    count = list(Counter(nums))
    count_num = len(count)

    if (length <= count_num):
        answer = length
    else:
        answer = count_num

    return answer
