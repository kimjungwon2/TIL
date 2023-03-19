def solution(genres, plays):
    answer = []
    album = dict()
    album_sum = dict()

    for index, (i, j) in enumerate(zip(genres, plays)):
        if (i not in album):
            album[i] = [(index, j)]
            album_sum[i] = j
        else:
            album[i].append((index, j))
            album_sum[i] += j

    for i in album:
        album[i] = sorted(album[i], key=lambda x: x[1], reverse=True)

    max_value = []

    for i, j in zip(album_sum.keys(), album_sum.values()):
        max_value.append((i, j))

    max_value = sorted(max_value, key=lambda x: x[1], reverse=True)

    for i in max_value:
        for j in range(2):
            if (len(album[i[0]]) == 1):
                answer.append(album[i[0]][j][0])
                break
            else:
                answer.append(album[i[0]][j][0])

    return answer
