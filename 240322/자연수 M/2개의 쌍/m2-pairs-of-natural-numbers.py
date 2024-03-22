import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    for i in range(x):
        nums.append(y)

nums.sort()

max_sum = 0

left = 0
right = len(nums)-1

while left < right:
    max_sum = max(max_sum,nums[left]+nums[right])
    left += 1
    right -= 1

print(max_sum)