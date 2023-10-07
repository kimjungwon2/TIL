from collections import defaultdict


def solution(today, terms, privacies):
    answer = []

    period = defaultdict(lambda: 0)

    year, month, day = map(int, today.split('.'))

    for term in terms:
        a, b = term.split()
        period[a] = int(b)

    index = 1

    for privacy in privacies:
        day, term = privacy.split()

        t_year, t_month, t_day = map(int, day.split('.'))

        sum_day = (year-t_year)*12*28+(month-t_month)*28+(day-t_day)

        if (period[term]*28 >= sum_day):
            answer.append(index)

        index += 1

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], [
      "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
