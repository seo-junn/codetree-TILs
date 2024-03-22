import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
base = Counter(nums)
index = list(sorted(base.keys()))

if len(index) == 1 or base[index[1]] > 1: print(-1)
else:
    target = index[1]
    for i in range(n):
        if nums[i] == target:
            print(i+1)
            break