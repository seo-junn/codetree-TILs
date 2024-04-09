import sys
from collections import Counter

n,m = map(int,sys.stdin.readline().split())
base = Counter(list(map(int,sys.stdin.readline().split())))
ans = []
for num in map(int,sys.stdin.readline().split()):
    ans.append(base[num] if num in base else 0)

print(*ans)