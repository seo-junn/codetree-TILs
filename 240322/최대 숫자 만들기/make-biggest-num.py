import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())
nums = sys.stdin.read().splitlines()

nums.sort(key=lambda x:x*10,reverse=True)
print(''.join(nums))