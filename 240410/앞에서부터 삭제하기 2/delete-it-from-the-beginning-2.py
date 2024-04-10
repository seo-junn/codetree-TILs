import sys
import heapq

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

max_avg = 0
for K in range(1,n-1):
    arr = nums[K:]
    heapq.heapify(arr)
    heapq.heappop(arr)
    avg = sum(arr)/len(arr)
    max_avg = max(max_avg,avg)

print("%.2f"%max_avg)