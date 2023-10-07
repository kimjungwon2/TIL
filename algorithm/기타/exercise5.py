def solution(num, k):
    num_list = []

    i = str(num)

    for s in i:
        num_list.append(int(s))

    length = len(num_list)

    for t in range(length):
        print(t)
        if (num_list[t] == k):
            return t+1
            
    return -1

ans = solution(29183,1)

print(ans)