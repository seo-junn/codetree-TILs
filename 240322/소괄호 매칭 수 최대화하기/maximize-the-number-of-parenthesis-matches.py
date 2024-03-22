import sys
from functools import cmp_to_key

def compare(x, y):
    if x + y < y + x:
        return -1
    if x + y > y + x:
        return 1
    return 0

N = int(sys.stdin.readline())
chunks = sys.stdin.read().splitlines()
chunks.sort(key=cmp_to_key(compare))
res = ''.join(chunks)

score = 0
for i in range(len(res)):
    if res[i] == '(':
        for j in range(i+1,len(res)):
            if res[j] == ')':
                score += 1

print(score)