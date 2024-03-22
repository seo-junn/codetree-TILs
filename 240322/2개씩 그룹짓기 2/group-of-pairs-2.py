import sys

n = int(sys.stdin.readline())
nums = list(sorted(map(int,sys.stdin.readline().split())))

diff = sys.maxsize
for i in range(n):
    diff = min(diff,nums[n+i]-nums[i])

print(diff)