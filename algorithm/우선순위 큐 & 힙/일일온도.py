def daily(list):
    answer = [0]*len(list)
    stack = []
    for i, cur in enumerate(list):
        while stack and cur >list[stack[-1]]:
            last= stack.pop()
            answer[last]=i-last
            stack.append(i)
        
    return answer