array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

length = len(array)

for i in range(length):
    min_index = i

    for j in range(i+1, length):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)
