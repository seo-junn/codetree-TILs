import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
A = [sys.stdin.readline().strip() for _ in range(N)]
B = [sys.stdin.readline().strip() for _ in range(N)]

count = 0
base = set()
for item in combinations(range(M),3):
    idx1,idx2,idx3 = item
    base.clear()
    for i in range(N):
        base.add(A[i][idx1]+A[i][idx2]+A[i][idx3])

    possible = True
    for i in range(N):
        if B[i][idx1] + B[i][idx2] + B[i][idx3] in base:
            possible = False
            break
    if possible: count += 1

print(count)