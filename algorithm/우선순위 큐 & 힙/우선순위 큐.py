import heapq

pq = []

heapq.heappush(pq, 4)
heapq.heappush(pq,12)
heapq.heappush(pq,0)
heapq.heappush(pq,-5)
heapq.heappush(pq,8)

print(pq)

while pq:
    print(pq[0])
    heapq.heappop(pq)
    