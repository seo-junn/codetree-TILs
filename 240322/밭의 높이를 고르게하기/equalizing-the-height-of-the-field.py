N, H, T = map(int,input().split())
heights = list(map(int,input().split()))

ans = 10**7
for i in range(N-T+1):
    cost = 0
    for t in range(T):
        cost += abs(heights[i+t]-H)
    ans = min(ans,cost)

print(ans)