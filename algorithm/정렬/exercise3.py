array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 하나의 원소만 있으면 종료.
    if len(array) <= 1:
        return array

    pivot = array[0]
    a = array[1:]

    left = [x for x in a if x<=pivot]
    right= [x for x in a if x>pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)


print(quick_sort(array))
