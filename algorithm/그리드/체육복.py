def solution(n, lost, reserve):
    reserve = [r for r in reserve if r not in lost]
    lost = [l for l in lost if l not in reserve]
    for r in reserve:
        f = r - 1
        b = r + 1
        if f in lost:
            lost.remove(f)
        elif b in lost:
            lost.remove(b)
    return n - len(lost)
