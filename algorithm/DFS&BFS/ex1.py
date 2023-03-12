def solution(priorities, location):
    answer = 0
    arr = []
    length = len(priorities)

    while (True):
        max_value = max(priorities)

        for i, j in enumerate(priorities):
            if (max_value == j and max_value != 0):
                arr.append((j, i))
                priorities[i] = 0
                max_value = max(priorities)

        if (len(arr) == length):
            break

    for i, j in enumerate(arr):
        if (j[1] == location):
            answer = i+1

    return answer
