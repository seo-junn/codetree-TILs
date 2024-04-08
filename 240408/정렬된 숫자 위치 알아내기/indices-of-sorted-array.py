import sys

N = int(sys.stdin.readline())
base = []

idx = 1
for num in map(int,sys.stdin.readline().split()):
    base.append((num,idx))
    idx += 1

base.sort()

ans = [0]*N
for i in range(N):
    ans[base[i][1]-1] = i+1

print(*ans)