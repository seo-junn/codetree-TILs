import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
A = [sys.stdin.readline().strip() for _ in range(N)]
B = [sys.stdin.readline().strip() for _ in range(N)]

count = 0
for item in combinations(range(M),3):
    idx1,idx2,idx3 = item
    A_set = set(map(lambda x:(x[idx1],x[idx2],x[idx3]),A))
    B_set = set(map(lambda x:(x[idx1],x[idx2],x[idx3]),B))
    if A_set.isdisjoint(B_set): count += 1

print(count)