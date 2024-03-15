import sys

n, s = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

length = n
start = 0
end = 0
total = 0

while end < n:
    total += nums[end]
    while total >= s:
        length = min(length,end-start+1)
        total -= nums[start]
        start += 1
    end += 1

print(length)