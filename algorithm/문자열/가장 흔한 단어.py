from collections import Counter


def most(str, ban):
    k= str.replace(',', '', 1000)
    j= k.replace('.', '', 1000)

    s = j.lower().split()

    a = Counter(s)

    c = a.most_common(2)
    b = a.most_common(2)[0][0]

    if b == ban:
        return a.most_common(2)[1][0]

    return b


print(most("Bob hit a ball, the hit BALL flew far after it was hit.", "hit"))
