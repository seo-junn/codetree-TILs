import sys

N, K = map(int,sys.stdin.readline().split())
nums = list(sorted(map(int,sys.stdin.read().splitlines())))

start = 0
end = 0
cand = []
count = 0

while end < N:
    if nums[end] - nums[start] <= K:
        count += 1
        end += 1
    else:
        cand.append(count)
        count = 0
        start = end

cand.append(count)
cand.sort()

print(cand[-1]+cand[-2])