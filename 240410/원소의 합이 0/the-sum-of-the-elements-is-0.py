import sys
from collections import Counter

n = int(sys.stdin.readline())
A = Counter(map(int,sys.stdin.readline().split()))
B = Counter(map(int,sys.stdin.readline().split()))
C = Counter(map(int,sys.stdin.readline().split()))
D = Counter(map(int,sys.stdin.readline().split()))

count = 0
for a in A.keys():
    for b in B.keys():
        for c in C.keys():
            d = 0 - a - b - c
            if d in D:
                count += A[a]*B[b]*C[c]*D[d]

print(count)