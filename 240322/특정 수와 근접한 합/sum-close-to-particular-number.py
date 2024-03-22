import sys

N, S = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

base = sum(nums)
ans = sys.maxsize

for i in range(N):
    for j in range(i+1,N):
        temp = base-nums[i]-nums[j]
        ans = min(ans,abs(temp-S))

print(ans)