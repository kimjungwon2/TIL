def solution(s):
    answer = 0
    arr = []
    array_s = s.split(" ")

    for i in array_s:
        if (i == 'Z'):
            length = len(arr)

            if (length == 0):
                continue
            else:
                del (arr[length-1])

        else:
            arr.append(int(i))

    answer = sum(arr)

    return answer

ans = solution("-20 -20 Z Z 5")
print(ans)
