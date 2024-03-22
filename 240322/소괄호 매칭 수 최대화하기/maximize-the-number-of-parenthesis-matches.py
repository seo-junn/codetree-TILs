import sys
from functools import cmp_to_key

def compare(x, y):
    if x[0]*y[1] > x[1]*y[0]:
        return -1
    if x[0]*y[1] < x[1]*y[0]:
        return 1
    return 0

n = int(sys.stdin.readline())

score = 0
chunks = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    lc,rc = 0,0
    for c in line:
        if c == '(': lc += 1
        else:
            rc += 1
            score += lc
    
    chunks.append((lc,rc))

chunks.sort(key=cmp_to_key(compare))

for i in range(n):
    for j in range(i+1,n):
        score += chunks[i][0]*chunks[j][1]

print(score)