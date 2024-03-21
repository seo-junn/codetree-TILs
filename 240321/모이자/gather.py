import sys
n = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))

min_dist = 10*7

for target in range(n):
    dist = 0
    for i in range(n):
        dist += abs(target-i)*people[i]
    if min_dist > dist:
        min_dist = dist

print(min_dist)