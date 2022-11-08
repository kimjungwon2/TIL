def solution(genres, plays):
    data = dict()
    sum_data = dict()
    length = len(genres)
    answer = []

    for i in range(length):
        if (genres[i] not in data):
            data[genres[i]] = [[plays[i], i]]
            sum_data[genres[i]] = [plays[i]]
        else:
            data[genres[i]].append([plays[i], i])
            sum_data[genres[i]].append(plays[i])

    #합계 구하기
    for i in sum_data:
        sum_data[i] = sum(sum_data[i])

    #재생수 별로 배열
    for i in data:
        data[i] = sorted(data[i], reverse=True)

    sum_data = sorted(sum_data, key=lambda x: sum_data[x], reverse=True)

    for i in sum_data:
        for j in range(0, 2):
            if (len(data[i]) < 2 and j == 1):
                break

            if (j == 0 and len(data[i]) >= 2 and data[i][0][0] == data[i][1][0]):
                s = min(data[i][0][1], data[i][1][1])
                m = max(data[i][0][1], data[i][1][1])
                answer.append(s)
                answer.append(m)
                break
            elif (j == 1 and len(data[i]) > 2 and data[i][1][0] == data[i][2][0]):
                s = min(data[i][1][1], data[i][2][1])
                answer.append(s)
            else:
                answer.append(data[i][j][1])

    return answer
