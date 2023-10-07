import heapq

def heapsort(n):
    h=[]
    result =[]

    #원소를 힙에 삽입
    for value in n:
        heapq.heappush(h,value)

    #힙에 삽입된 모든 원소를 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])