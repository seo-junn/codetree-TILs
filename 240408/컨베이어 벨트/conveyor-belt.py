import sys
from collections import deque

n, t = map(int,sys.stdin.readline().split())
line1 = deque(list(map(int,sys.stdin.readline().split())))
line2 = deque(list(map(int,sys.stdin.readline().split())))

for _ in range(t):
    line1.appendleft(line2.pop())
    line2.appendleft(line1.pop())

print(*line1)
print(*line2)