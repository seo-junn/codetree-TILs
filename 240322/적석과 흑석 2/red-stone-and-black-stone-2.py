import sys
from bisect import bisect_left

C, N = map(int,sys.stdin.readline().split())
reds = [int(sys.stdin.readline()) for _ in range(C)]
blacks = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

reds.sort()
cache = [0]*C
blacks.sort(key=lambda x:(x[1]-x[0],x[0]))

count = 0
for lb,rb in blacks:
    l_idx = bisect_left(reds,lb)
    r_idx = bisect_left(reds,rb)
    for idx in range(l_idx,r_idx):
        if cache[idx] == 0 and lb <= reds[idx] <= rb:
            cache[idx] += 1
            count += 1
            break

print(count)