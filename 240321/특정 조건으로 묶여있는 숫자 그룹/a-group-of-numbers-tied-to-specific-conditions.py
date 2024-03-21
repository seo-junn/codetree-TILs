import sys

N, K = map(int,sys.stdin.readline().split())
nums = list(sorted(map(int,sys.stdin.read().splitlines())))

L, R = [0]*N, [0]*N

count = 0
i = 0
for j in range(N):
    while i < N and nums[j]-nums[i] > K:
        i += 1
    
    count = max(count, j - i + 1)

    L[j] = count

count = 0
j = N-1
for i in range(N-1,-1,-1):
    while j - 1 >= i and nums[j]-nums[i] > K:
        j -= 1
    
    count = max(count, j - i + 1)

    R[i] = count

ans = L[N-1]
for i in range(N-1):
    ans = max(ans,L[i]+R[i+1])

print(ans)