import sys

N, K = map(int,sys.stdin.readline().split())
line = [0]*10001
sc = {'G':1,'H':2}

for _ in range(N):
    pos, ch = sys.stdin.readline().split()
    line[int(pos)] += sc[ch]

now = sum(line[1:K+2])
ans = now
start = 1
end = K+2

while end < 10001:
    now -= line[start]
    now += line[end]
    ans = max(ans,now)
    start += 1
    end += 1

print(ans)