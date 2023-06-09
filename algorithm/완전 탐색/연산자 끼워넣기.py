N = int(input())
arr = list(map(int,input().split()))
# +/-/x/나눗셈
plus, minus,multiply,divide = map(int, input().split())


max_v = -1000000000
min_v = 1000000000

def recursive(num,result):
    global plus, minus,multiply,divide,max_v,min_v

    if num == N-1:
        max_v = max(max_v,result)
        min_v = min(min_v,result)
        return 
    
    if plus>0:
        plus-=1
        recursive(num+1,result+arr[num+1])
        plus+=1
    if minus > 0:
        minus -= 1
        recursive(num+1, result-arr[num+1])
        minus += 1
    if multiply > 0:
        multiply -= 1
        recursive(num+1, result*arr[num+1])
        multiply += 1
    if divide > 0:
        divide -= 1

        if result >0:
            recursive(num+1, result//arr[num+1])
            divide += 1
        else:
            recursive(num+1, (-1*result//arr[num+1])*-1)
            divide += 1


recursive(0,arr[0])

print(max_v)
print(min_v)