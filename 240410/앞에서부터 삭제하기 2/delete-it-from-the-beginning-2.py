import sys
import heapq

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
min_val = [0]*n
arr = []
total = 0
for i in range(n-1,-1,-1):
    total += nums[i]
    heapq.heappush(arr,nums[i])
    min_val[i] = arr[0]

max_avg = 0
for k in range(1,n-1):
    total -= nums[k-1]
    avg = (total-min_val[k])/(n-1-k)
    max_avg = max(max_avg,avg)

print("%.2f"%max_avg)