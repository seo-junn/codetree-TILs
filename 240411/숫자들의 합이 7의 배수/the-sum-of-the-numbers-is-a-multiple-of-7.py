import sys

N = int(sys.stdin.readline())
nums = [0] + list(map(int,sys.stdin.read().splitlines()))

starts = [0] + [sys.maxsize]*6
ends = [0] + [-sys.maxsize]*6

acc = 0
for i in range(1,N+1):
    acc += nums[i]
    acc %= 7

    starts[acc] = min(starts[acc],i)
    ends[acc] = max(ends[acc],i)

ans = 0
for i in range(6):
    ans = max(ans,ends[i]-starts[i])

print(ans)