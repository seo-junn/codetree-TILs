import sys

N = int(sys.stdin.readline())
blocks = list(map(int,sys.stdin.read().splitlines()))

std = 0
for i in range(N): std += blocks[i]
std //= N

count = 0
for i in range(N):
    count += abs(blocks[i]-std)

print(count//2)