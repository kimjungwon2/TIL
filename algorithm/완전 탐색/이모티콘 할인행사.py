from itertools import product

def solution(users, emoticons):
    length = len(emoticons)
    discounts = [10, 20, 30, 40]
    answer = [0, 0]
    d = product(discounts, length)

    return answer


solution([[40, 2900], [23, 10000], [11, 5200], [
         5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])