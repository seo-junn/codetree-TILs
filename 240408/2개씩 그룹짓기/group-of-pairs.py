import sys

N = int(sys.stdin.readline())
nums = list(sorted(map(int,sys.stdin.readline().split())))

max_sum = 0
for i in range(N):
    temp = nums[i] + nums[2*N-1-i]
    max_sum = max(max_sum,temp)

print(max_sum)