import sys
import heapq

n,m,k = map(int,sys.stdin.readline().split())
arr1 = list(sorted(map(int,sys.stdin.readline().split())))
arr2 = list(sorted(map(int,sys.stdin.readline().split())))

l,r,comb_num = 0,0,0

while l < n and r < m and l*r < k:
    if arr1[l] <= arr2[r]: l += 1
    else: r += 1

if l == n and l*r < k:
    while r < m and l*r < k: r += 1
if r == m and l*r < k:
    while l < n and l*r < k: l += 1

base = []
for i in range(l):
    for j in range(r):
        heapq.heappush(base,-(arr1[i]+arr2[j]))

for _ in range(l*r-k): heapq.heappop(base)
print(-base[0])