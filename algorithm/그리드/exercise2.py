n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k  # 이러면 n이 k로 나누어지지 않을 때, 가장 가까운 k가 어떤 건지 알 수 있다.
    result += (n-target)  # result는 연산 횟수이다.
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)
