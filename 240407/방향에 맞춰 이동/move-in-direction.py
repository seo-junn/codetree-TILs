import sys

dx = {'N':0,'E':1,'S':0,'W':-1}
dy = {'N':1,'E':0,'S':-1,'W':0}

px,py = 0,0

for _ in range(int(sys.stdin.readline())):
    direct,dist = sys.stdin.readline().split()
    px += dx[direct]*int(dist)
    py += dy[direct]*int(dist)

print(px,py)