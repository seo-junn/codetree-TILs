import sys

N = int(sys.stdin.readline())
people = list(map(int,sys.stdin.read().splitlines()))

dist = sys.maxsize
for offset in range(N):
    temp = 0
    for i in range(N):
        temp += ((offset+i)%N)*people[i]
    dist = min(dist,temp)

print(dist)