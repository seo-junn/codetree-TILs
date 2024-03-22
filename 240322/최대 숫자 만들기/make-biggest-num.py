import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())
nums = sys.stdin.read().splitlines()

def compare(x, y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else: return 0

nums.sort(key=cmp_to_key(compare))
print(''.join(nums))