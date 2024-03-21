import sys

N, K = map(int,sys.stdin.readline().split())
nums = list(sorted(map(int,sys.stdin.read().splitlines())))

start = 0
end = 0
cand = []

while end < N:
    if nums[end] - nums[start] <= K:
        end += 1
    else:
        cand.append(end-start)
        while nums[end] - nums[start] > K:
            start += 1

cand.append(end-start)
cand.sort()

print(cand[-1]+cand[-2])