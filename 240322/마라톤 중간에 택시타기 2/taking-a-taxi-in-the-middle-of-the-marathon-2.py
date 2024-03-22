import sys

N = int(sys.stdin.readline())
points = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

dist = sys.maxsize

for target in range(1,N-1):
    temp = 0
    px,py = points[0]
    for i in range(1,N):
        if i == target: continue
        nx, ny = points[i]
        temp += abs(px-nx)+abs(py-ny)
        px,py = nx,ny
    dist = min(dist,temp)

print(dist)