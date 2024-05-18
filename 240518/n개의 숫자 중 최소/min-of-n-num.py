from collections import Counter

n = int(input())
base = Counter(map(int,input().split()))
key = min(base.keys())
print(key,base[key])