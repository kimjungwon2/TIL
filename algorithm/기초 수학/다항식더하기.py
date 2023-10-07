def solution(polynomial):
    arr = polynomial.split(" ")

    x_value = 0
    digit = 0

    for i in arr:
        if (i.isdigit()):
            digit += int(i)
        elif (i == '+'):
            continue
        else:
            if (i == 'x'):
                x_value += 1
            else:
                value = i.replace('x', '')
                x_value += int(value)

    answer = ''

    if (x_value == 1 and digit == 0):
        answer += 'x'
    elif (x_value == 1 and digit != 0):
        answer += 'x'+' + '+str(digit)
    elif (x_value != 0 and digit == 0):
        answer += str(x_value)+'x'
    elif (x_value != 0 and digit != 0):
        answer += str(x_value)+'x'+' + '+str(digit)
    elif (x_value == 0 and digit != 0):
        answer += str(digit)

    return answer
