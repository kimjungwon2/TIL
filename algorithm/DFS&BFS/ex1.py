def solution(sizes):
    x = []
    y = []

    for i in sizes:
        x.append(i[0])
        y.append(i[1])

    max_value = max(max(x), max(y))

    target = 0

    for i in sizes:
        if (max_value-i[0] < max_value-i[1]):
            if (target > i[1]):
                continue
            else:
                target = i[1]
        else:
            if (target > i[0]):
                continue
            else:
                target = i[0]

    return target*max_value
