import sys
from sortedcontainers import SortedSet


C, N = map(int,sys.stdin.readline().split())
reds = [int(sys.stdin.readline()) for _ in range(C)]
blacks = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

red = SortedSet(reds)
blacks.sort(key=lambda x:(x[1],x[0]))

count = 0
for lb, rb in blacks:
    idx = red.bisect_left(lb)
    if idx != len(red):
        t = red[idx]
        if t <= rb:
            count += 1
            red.remove(t)

print(count)