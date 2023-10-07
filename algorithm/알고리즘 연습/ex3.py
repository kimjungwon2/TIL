def solution(my_string):
    intch = "0"
    answer = 0
    for ch in my_string:
        if ch.isdigit():
            intch += ch
        else:
            answer += int(intch)
            intch = "0"
    answer += int(intch)
    return answer


ans = solution("aAb1B2cC34oOp")
print(ans)