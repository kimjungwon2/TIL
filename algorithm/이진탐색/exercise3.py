from bisect import bisect_left, bisect_right


def count_by_range(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index-left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 3~0인 데이터 개수 출력
print(count_by_range(a, 3, 9))
