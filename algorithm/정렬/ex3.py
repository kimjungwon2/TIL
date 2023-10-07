n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

array = sorted(array, key=lambda x: x[1])

for i in range(len(array)):
    print(array[i][0],end=' ')