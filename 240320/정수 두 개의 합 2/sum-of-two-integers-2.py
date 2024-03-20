import sys

n, k = map(int,sys.stdin.readline().split())
nums = list(sorted(map(int,sys.stdin.read().splitlines())))

start = 0
end = n-1
count = 0

while start < end:
    while nums[end] > k-nums[start]:
        end -= 1
    
    count += end-start
    start += 1

print(count)