import sys
from collections import deque

n,t = map(int,sys.stdin.readline().split())
line1 = deque(map(int,sys.stdin.readline().split()))
line2 = deque(map(int,sys.stdin.readline().split()))
line3 = deque(map(int,sys.stdin.readline().split()))

for _ in range(t):
    line1.appendleft(line3.pop())
    line2.appendleft(line1.pop())
    line3.appendleft(line2.pop())

print(*line1)
print(*line2)
print(*line3)