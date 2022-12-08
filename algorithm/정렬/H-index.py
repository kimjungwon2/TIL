def solution(citations):
    citations.sort(reverse=True)

    answer = 0
    arr = []

    for i, j in enumerate(citations):
        if (i >= j):
            arr.append(i)
            break

    if (len(arr) == 0):
        return len(citations)
    else:
        return arr[0]
