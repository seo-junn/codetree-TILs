import sys

n, m = map(int,sys.stdin.readline().split())
fire = list(sorted(map(int,sys.stdin.readline().split())))
fighter = list(sorted(map(int,sys.stdin.readline().split())))

j = 0
length = 0
for i in range(len(fire)):
    dist = 2*10**9
    while j < len(fighter) and dist > abs(fire[i]-fighter[j]):
        dist = abs(fire[i]-fighter[j])
        j += 1
    j -= 1
    length = max(length,dist)

print(length)