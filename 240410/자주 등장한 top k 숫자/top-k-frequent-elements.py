import sys
from collections import Counter

n,k = map(int,sys.stdin.readline().split())
base = Counter(map(int,sys.stdin.readline().split()))
base = list(map(lambda x:(base[x],x),base.keys()))
base.sort(key=lambda x:(-x[0],-x[1]))
base = list(map(lambda x:x[1],base))
print(*base[:k])