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

            if (len(data[i][j]) > 2 and data[i][j][0] == data[i][j+1][0]):
                print('출력')
                s = min(data[i][j][1], data[i][j+1][1])
                answer.append(s)
            else:
                answer.append(data[i][j][1])

    return answer


solution(["classic", "pop", "classic", "classic", "pop", "rock"],
         [500, 600, 150, 800, 2500, 900])
