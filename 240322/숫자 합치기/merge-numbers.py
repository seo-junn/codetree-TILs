import sys
import heapq

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()

cost = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    cost += a+b
    heapq.heappush(nums,a+b)

print(cost)