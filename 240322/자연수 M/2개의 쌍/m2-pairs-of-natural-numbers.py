import sys

N = int(sys.stdin.readline())
nums = {}

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    nums[y] = x

index = list(sorted(nums.keys()))
left = 0
right = len(index)-1

max_sum = 0
while left < right:
    if nums[index[left]] and nums[index[right]]:
        max_sum = max(max_sum,index[left]+index[right])
        temp = min(nums[index[left]],nums[index[right]])
        nums[index[left]] -= temp
        nums[index[right]] -= temp
    elif nums[index[left]] == 0:
        left += 1
    else:
        right -= 1

print(max_sum)