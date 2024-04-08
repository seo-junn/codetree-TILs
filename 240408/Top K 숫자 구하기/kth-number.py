import sys

N, K = map(int,sys.stdin.readline().split())
nums = list(sorted(map(int,sys.stdin.readline().split())))

print(nums[K-1])