def solution(cap, n, deliveries, pickups):
    idps = []

    for i, (d, p) in enumerate(zip(deliveries, pickups), 1):
        if d or p:
            idps.append((i, d, p))

    delivery = 0
    pickup = 0
    answer = 0

    while idps:
        i, d, p = idps.pop()
        delivery += d
        pickup += p

        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += 2*i

    return answer

solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0])