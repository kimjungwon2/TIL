N = int(input())
req = list(map(int,input().split()))
M = int(input())

low = 0
high = max(req)

mid = (low+high)//2
ans =0 

def is_possible(mid):
    tot = 0 
    for r in req:
        tot+=min(r, mid)

    

while low <=high:
    if is_possible(mid):
        low = mid+1
        ans = mid 
    else: 
        high = mid-1

    mid =(low+high)//2 