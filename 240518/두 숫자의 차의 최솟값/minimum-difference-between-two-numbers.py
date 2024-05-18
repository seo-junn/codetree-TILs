n = int(input())
nums = list(map(int,input().split()))

min_diff = 101
for i in range(1,n):
    diff = nums[i]-nums[i-1]
    if diff < min_diff:
        min_diff = diff

print(min_diff)