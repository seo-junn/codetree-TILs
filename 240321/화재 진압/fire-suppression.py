import sys

n, m = map(int,sys.stdin.readline().split())
fire = list(sorted(map(int,sys.stdin.readline().split())))
fighter = list(sorted(map(int,sys.stdin.readline().split())))

length = 0
ff_idx = 0

for i in range(len(fire)):
    dist = abs(fighter[ff_idx] - fire[i])
    if ff_idx < len(fighter)-1:
        dist2 = abs(fighter[ff_idx+1]-fire[i])
        if dist2 < dist:
            dist = dist2
            ff_idx += 1

    length = max(length,dist)

print(length)