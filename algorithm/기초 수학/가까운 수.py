def solution(array, n):
    array.sort()
    abs_array = []

    for i in array:
        abs_array.append(abs(n-i))

    min_index = abs_array.index(min(abs_array))
    answer = array[min_index]

    return answer

