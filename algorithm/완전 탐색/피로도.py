from itertools import permutations


def solution(k, dungeons):
    answer = -1
    length = len(dungeons)

    perm = permutations(dungeons, length)

    for p in perm:
        have = k
        count = 0
        for i in range(length):
            if (have >= p[i][0] and have >= p[i][1]):
                have -= p[i][1]
                count += 1
        answer = max(answer, count)

    return answer
