import sys

n = int(sys.stdin.readline())
nums = list(sorted(map(int,sys.stdin.readline().split())))
cand = [nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1]]
print(max(cand))