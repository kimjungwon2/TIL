array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):

    #리스트가 하나의 원소만 담으면 종료
    if(len(array)<=1):
        return array
    
    pivot = array[0]
    a = array[1:]

    left_side = [x for x in a if x<=pivot]
    right_side = [x for x in a if x>pivot]

    return quick_sort(left_side)+ [pivot]+quick_sort(right_side)

print(quick_sort(array))