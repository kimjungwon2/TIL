from itertools import product


def solution(word):
    data = dict()
    alpha = ['A', 'E', 'I', 'O', 'U']
    count = 0
    word_sort = []

    print(list(map(''.join, product(alpha, repeat=2))))

    for i in range(1, 6):
        for c in product(alpha, repeat=i):
            word_sort.append(''.join(c))

    word_sort.sort()

    return word_sort.index(word)+1
