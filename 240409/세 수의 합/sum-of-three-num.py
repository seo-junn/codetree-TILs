import sys

n,k = map(int,sys.stdin.readline().split())
base = {}
for num in map(int,sys.stdin.readline().split()):
    if num in base: base[num] += 1
    else: base[num] = 1

count = 0
for a in base.keys():
    common = 0
    for b in base.keys():
        c = k-a-b
        if c in base:
            if a == b == c:
                count += base[a]*(base[a]-1)*(base[a]-2)
            elif a == b:
                count += base[a]*(base[a]-1)*base[c]
            elif b == c:
                count += base[b]*(base[b]-1)*base[a]
            elif a == c:
                count += base[a]*(base[a]-1)*base[b]
            else:
                count += base[a]*base[b]*base[c]

print(count//6)