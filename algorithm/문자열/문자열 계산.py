def solution(my_string):
    strings = my_string.split(' ')

    count = int(strings[0])

    length = len(strings)

    for i in range(1, length):
        if (strings[i] == '+'):
            count += int(strings[i+1])
        elif (strings[i] == '-'):
            count -= int(strings[i+1])

    return count
