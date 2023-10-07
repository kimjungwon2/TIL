from itertools import product

from itertools import product


def solution(users, emoticons):
    answer = []
    length = len(emoticons)
    ratio = [10, 20, 30, 40]

    max_price = 0
    max_member = 0

    for pro in product(ratio, repeat=length):
        sum_v = 0
        member = 0

        for user in users:
            p_ratio, price = user[0], user[1]
            pay = 0

            for i, emoticon in enumerate(emoticons):
                if (pro[i] >= p_ratio):
                    pay += emoticon*(100-pro[i]) // 100

            if (pay >= price):
                member += 1
            else:
                sum_v += pay

        answer = max(answer, [member, sum_v])

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
