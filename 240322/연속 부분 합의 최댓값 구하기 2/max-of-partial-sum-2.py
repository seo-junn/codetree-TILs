import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

now = nums[0]
ans = now

for i in range(1, n):
    if now < 0:
        now = nums[i]
    else:
        now += nums[i]
    ans = max(ans,now)

print(ans)