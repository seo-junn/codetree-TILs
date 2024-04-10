import sys

n = int(sys.stdin.readline())
base = {}

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x in base:
        if base[x] > y: base[x] = y
    else: base[x] = y

print(sum(base.values()))