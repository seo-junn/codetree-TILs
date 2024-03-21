import sys

n, m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

if n < 2*m:
    print(-1)
    exit(0)

left, right = 0, 0
length = n
in_group = False
out_group = False

cache = [0]*(m+1)
start,end,count = 0,0,0
while end < n:
    if count == m:
        if length > end - start:
            length = end-start
            left,right = start,end
            in_group = True
        cache[nums[start]] -= 1
        if cache[nums[start]] == 0:
            count -= 1
        start += 1
    else:
        if cache[nums[end]] == 0:
            count += 1
        cache[nums[end]] += 1
        end += 1

if count == m:
    if length > end-start:
        length = end - start
        left, right = start,end
        in_group = True

cache = [0]*(m+1)
count = 0
for item in nums[:left] + nums[right:]:
    if cache[item] == 0:
        count += 1
        cache[item] += 1
    if count == m:
        out_group = True
        break

if in_group and out_group: print(length)
else: print(-1)