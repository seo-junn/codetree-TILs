import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

ans = 0

for i in range(n-1):
    for j in range(i+2,n):
        ans = max(ans,nums[i]+nums[j])

print(ans)