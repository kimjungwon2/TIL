def solution(score):
    average_score = []
    data = dict()
    answer = []

    for i in score:
        average_score.append((i[0]+i[1])/2)

    average_score.sort(reverse=True)

    ranking = 0
    duplicate = 0

    for i in average_score:
        if i not in data:
            if (duplicate == 0):
                ranking += 1
                data[i] = ranking
            else:
                ranking += duplicate+1
                data[i] = ranking
                duplicate = 0
        else:
            data[i] = ranking
            duplicate += 1

    for i in score:
        answer.append(data[(i[0]+i[1])/2])

    return answer
