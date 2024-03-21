import sys
from sortedcontainers import SortedSet

N, D = map(int,sys.stdin.readline().split())
dots = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
dots.sort()

dot_count = SortedSet()

def get_min():
    if not dot_count: return 0
    return dot_count[0][0]

def get_max():
    if not dot_count: return 0
    return dot_count[-1][0]

dist = 10**7

j = 0
for i in range(N):
    while j < N and get_max() - get_min() < D:
        dot_count.add((dots[j][1],dots[j][0]))
        j += 1
    
    if get_max() - get_min() < D:
        break
    
    dist = min(dist, dots[j-1][0]-dots[i][0])

    dot_count.remove((dots[i][1],dots[i][0]))

if dist == 10**7: print(-1)
else: print(dist)