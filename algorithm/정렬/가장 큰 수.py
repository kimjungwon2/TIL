from itertools import permutations


def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x*3, reverse=True)

    answer = str(int(''.join(str_numbers)))

    return answer


solution([3, 30, 34, 5, 9])
