import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

count = 0
for i in range(N):
    for j in range(i,N):
        val = sum(nums[i:j+1])/(j-i+1)
        for idx in range(i,j+1):
            if nums[idx] == val:
                count += 1
                break

print(count)