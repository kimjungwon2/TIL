def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in dic:
            dic[g].append((i, p))
        else:
            dic[g] = [(i, p)]

        if g in dic2:
            dic2[g] += p
        else:
            dic2[g] = p

    for (k, _) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dic[k], key=lambda x: (x[1], -x[0]), reverse=True)[:2]:
            answer.append(i)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
      [500, 2500, 150, 800, 2500]))
