array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 하나의 원소만 있으면 종료.
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 피벗의 왼쪽부분
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행. 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
