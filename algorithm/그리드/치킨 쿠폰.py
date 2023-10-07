def solution(chicken):
    coupon = 0
    answer = 0

    coupon += chicken
    answer += chicken//10
    coupon = chicken % 10+answer

    while (True):
        if (coupon < 10):
            break
        answer += coupon//10
        coupon = coupon % 10 + coupon//10

    return answer
