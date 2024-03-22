n = int(input())

if n < 6:
    base = [-1,-1,1,-1,2,1]
    print(base[n])
else:
    dp = [-1]*(n+1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6,n+1):
        cand = []
        if dp[i-2] != -1: cand.append(dp[i-2])
        if dp[i-5] != -1: cand.append(dp[i-5])
        if cand: dp[i] = min(cand)+1

    print(dp[-1])