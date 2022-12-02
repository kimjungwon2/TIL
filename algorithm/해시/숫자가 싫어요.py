def solution(numbers):
    answer = 0
    data = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    key_list = data.keys()

    for i in key_list:
        numbers = numbers.replace(i, data[i])

    answer = int(numbers)

    return answer
