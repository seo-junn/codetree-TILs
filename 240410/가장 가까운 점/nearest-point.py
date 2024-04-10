import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
arr = []

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    heapq.heappush(arr,(x+y,x,y))

for _ in range(m):
    dumy,x,y = heapq.heappop(arr)
    x,y = x+2,y+2
    heapq.heappush(arr,(x+y,x,y))

print(arr[0][1],arr[0][2])