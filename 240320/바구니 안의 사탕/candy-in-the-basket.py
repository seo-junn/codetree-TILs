import sys

N, K = map(int,sys.stdin.readline().split())
candies = [0]*1000001
m_pos = 0

for _ in range(N):
    candy, pos = map(int,sys.stdin.readline().split())
    candies[pos] += candy
    m_pos = max(m_pos,pos)

now = sum(candies[:2*K+1])
start = 0
end = 2*K
ans = now

while end < m_pos+1:
    now -= candies[start]
    start += 1
    end += 1
    now += candies[end]
    if ans < now:
        ans = now

print(ans)