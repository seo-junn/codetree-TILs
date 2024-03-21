import sys

n, k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

cache = [0]*(max(nums)+1)

start = 0
end = 0
length = 0

while end < n:
    if cache[nums[end]] < k:
        cache[nums[end]] += 1
        end += 1
    else:
        length = max(length,end-start)
        while cache[nums[end]] >= k:
            cache[nums[start]] -= 1
            start += 1

length = max(length,end-start)
print(length)