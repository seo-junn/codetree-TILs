import sys

N = int(sys.stdin.readline())
points = []

for i in range(1,N+1):
    x,y = map(int,sys.stdin.readline().split())
    points.append((abs(x)+abs(y),i))

points.sort()

for item in points: print(item[1])