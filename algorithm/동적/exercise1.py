d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1

    # 계산한 문제면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 계산하지 않은 문제면 파보나치 결과 반환
    d[x] = fibo(x-1)+fibo(x-2)

    return d[x]


print(fibo(99))
