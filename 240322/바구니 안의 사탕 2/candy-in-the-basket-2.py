import sys

N, K = map(int,sys.stdin.readline().split())
basket = [0]*101

for _ in range(N):
    candy,pos = map(int,sys.stdin.readline().split())
    basket[pos] += candy

ans = 0
for c in range(100):
    temp = 0
    for i in range(c-K,c+K+1):
        if 0 <= i <= 100:
            temp += basket[i]
    ans = max(ans,temp)

print(ans)