import sys

n, m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
val = 0
count = 0

while end < n:
    if val < m:
        val += nums[end]
        end += 1
    elif val == m:
        count += 1
        val -= nums[start]
        start += 1
    else:
        while val > m:
            val -= nums[start]
            start += 1

if val == m: count += 1

print(count)