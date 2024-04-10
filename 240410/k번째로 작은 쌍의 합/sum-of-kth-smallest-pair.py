import sys
import heapq

n,m,k = map(int,sys.stdin.readline().split())
arr1 = list(sorted(map(int,sys.stdin.readline().split())))
arr2 = list(sorted(map(int,sys.stdin.readline().split())))

l,r = 0,0

base = []

for i in range(n):
    heapq.heappush(base,(arr1[i]+arr2[0],i,0))

for _ in range(k-1):
    dumy, i, j = heapq.heappop(base)

    j += 1
    if j < m:
        heapq.heappush(base, (arr1[i]+arr2[j],i,j))

ans,_,_ = heapq.heappop(base)

print(ans)