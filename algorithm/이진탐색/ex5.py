from bisect import bisect_left, bisect_right

def count_data(a,start,end):
    right = bisect_right(a, end)
    
    left = bisect_left(a, start)

    return right-left

a=[1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터 개수 출력
print(count_data(a,4,4))

#값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_data(a,-1,3))