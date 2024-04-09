import sys

n, k = map(int,sys.stdin.readline().split())
base = {}
for num in map(int,sys.stdin.readline().split()):
    if num in base: base[num] += 1
    else: base[num] = 1

count = 0
for key in base.keys():
    if k-key in base:
        count += base[key] * base[k-key]

print(count//2)