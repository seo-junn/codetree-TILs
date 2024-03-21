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
        cand.append((end-start,start,end-1))
        while nums[end] - nums[start] > K:
            start += 1

cand.append((end-start,start,end-1))
cand.sort()

ans = cand[-1][0]
for i in range(len(cand)-2,-1,-1):
    if cand[i][-1] < cand[-1][1] or cand[i][1] > cand[-1][-1]:
        ans += cand[i][0]
        break

print(ans)