import sys

n, k = map(int,sys.stdin.readline().split())

count = [set([i]) for i in range(n+1)]
positions = list(range(n+1))

commands = list(map(lambda x:tuple(map(int,x.split())), sys.stdin.read().splitlines()))
for _ in range(3):
    for a,b in commands:
        positions[a],positions[b] = positions[b],positions[a]
        count[positions[a]].add(a)
        count[positions[b]].add(b)

for i in range(1,n+1):
    print(len(count[i]))