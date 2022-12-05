def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if (s[i] == '('):
            stack.append('(')
        else:
            if (len(stack) == 0):
                return False
            stack.pop()

    if (len(stack) != 0):
        return False

    return True
