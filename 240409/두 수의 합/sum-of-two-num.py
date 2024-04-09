import sys

n, k = map(int,sys.stdin.readline().split())
base = {}
for num in map(int,sys.stdin.readline().split()):
    if num in base: base[num] += 1
    else: base[num] = 1

count = 0
for key in base.keys():
    t_key = k-key
    if k-key in base:
        if t_key != key:
            count += base[key] * base[k-key]
        else:
            count += base[key]*(base[key]-1)

print(count//2)