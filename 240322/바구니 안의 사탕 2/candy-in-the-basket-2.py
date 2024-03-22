import sys

N, K = map(int,sys.stdin.readline().split())
basket = [0]*101

for _ in range(N):
    candy,pos = map(int,sys.stdin.readline().split())
    basket[pos] += candy

now = sum(basket[:2*K+2])
ans = now
start = 0
end = 2*K+2

while end < N:
    now -= basket[start]
    now += basket[end]
    ans = max(ans,now)
    start += 1
    end += 1

print(ans)