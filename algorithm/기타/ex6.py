def solution(priorities, location):
    count = 0
    while True:
        x = priorities.pop(0)
        location -= 1
        if len(priorities) == 0:
            count += 1
            break

        if x >= sorted(priorities)[-1]:
            count += 1
            if location == -1:
                break
        else:
            priorities.append(x)

        if location == -1:
            location = len(priorities)-1

    return count


print(solution([1, 1, 9, 1, 1, 1],0))
