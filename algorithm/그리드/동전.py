N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()

num = 0

for coin in coins:
    num+=K // coin
    K%=coin

print(num)