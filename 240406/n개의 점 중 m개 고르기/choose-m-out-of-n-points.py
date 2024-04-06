import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())
dots = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]

min_dist_sq = sys.maxsize
for items in combinations(dots,m):
    max_dist_sq = 0
    for dot1,dot2 in combinations(items,2):
        max_dist_sq = max(max_dist_sq,(dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)
    min_dist_sq = min(min_dist_sq,max_dist_sq)

print(min_dist_sq)