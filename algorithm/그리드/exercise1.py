n= 1260
count = 0

array = [500,100,50,10]

for coin in array:
    count+=n // coin #동전 갯수 세기
    n%=coin

print(count)