import sys

n, s = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

start = 0
total = 0
length = n
for i in range(n):
    if total < s:
        total += nums[i]
    else:
        while total >= s:
            length = min(length,i-start)
            total -= nums[start]
            start += 1

print(length)