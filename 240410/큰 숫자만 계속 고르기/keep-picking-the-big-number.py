import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
arr = []
for num in map(int,sys.stdin.readline().split()):
    heapq.heappush(arr,-num)

for _ in range(m):
    heapq.heappush(arr,heapq.heappop(arr)+1)

print(-arr[0])