import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())
lines = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]

def check(lines):
    base = [[0]*(n+1) for _ in range(16)]
    for a, b in lines:
        base[b][a] = a+1
        base[b][a+1] = a
    res = []
    for l in range(1,n+1):
        current = l
        for h in range(1,16):
            if base[h][current]:
                current = base[h][current]
        res.append(current)
    return res

ans = check(lines)
count = len(lines)
find = False
for i in range(len(lines)):
    for item in combinations(lines,i):
        if ans == check(item):
            count = i
            find = True
            break
    if find: break

print(count)