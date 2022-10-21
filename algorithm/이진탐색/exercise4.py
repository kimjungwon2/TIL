n,m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

start = 0 
end = max(array)

result = 0 

while(start<=end):
    total=0
    mid=(start+end)//2

    for x in array:
        if x> mid:
            total+= x-mid

    #떡이 부족한 경우 왼쪽 탐색
    if total<m:
        end=mid - 1
    #떡이 충분한 경우 덜 짜르기(오른쪽 탐색) 
    else:
        result = mid #
        start = mid+1

print(result)