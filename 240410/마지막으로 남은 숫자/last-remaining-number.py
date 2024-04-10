import sys
import heapq

arr = []
n = int(sys.stdin.readline())
for num in map(int,sys.stdin.readline().split()):
    heapq.heappush(arr,-num)

while len(arr) > 1:
    a = -heapq.heappop(arr)
    b = -heapq.heappop(arr)
    diff = a-b
    if diff:
        heapq.heappush(arr,-diff)

print(-arr[0] if arr else -1)