import sys
from collections import Counter

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
C = list(map(int,sys.stdin.readline().split()))
D = list(map(int,sys.stdin.readline().split()))

base = {}
count = 0

for a in range(n):
    for b in range(n):
        val = A[a]+B[b]
        if val in base: base[val] += 1
        else: base[val] = 1

for c in range(n):
    for d in range(n):
        val = -C[c]-D[d]
        if val in base: count += base[val]

print(count)