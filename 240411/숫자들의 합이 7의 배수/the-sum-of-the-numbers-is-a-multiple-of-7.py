import sys

N = int(sys.stdin.readline())
nums = [0] + list(map(int,sys.stdin.read().splitlines()))

for i in range(1,N+1):
    nums[i] += nums[i-1]

for length in range(N,0,-1):
    for i in range(N-length+1):
        if (nums[i+length] - nums[i])%7 == 0:
            print(length)
            exit(0)