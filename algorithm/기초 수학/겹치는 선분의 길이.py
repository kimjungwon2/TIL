def solution(lines):
    result = []
    for a, b in lines:
        if a > b:
            a, b = b, a
        result += list(range(a, b))
    return sum(1 for i in set(result) if result.count(i) > 1)
