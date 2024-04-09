import sys

N = int(sys.stdin.readline())
x,y = map(lambda x:int(x)-1,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

time = 0
d = 0
cache = [[0]*N for _ in range(N)]
cache[x][y] = 1
failed = False
while 0 <= x < N and 0 <= y < N:
    rx,ry = x+dx[(d-1)%4],y+dy[(d-1)%4]
    if board[rx][ry] == '#':
        nx,ny = x+dx[d],y+dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == '#':
                d = (d+1)%4
                if cache[nx][ny] > 4:
                    failed = True
                    break
                cache[nx][ny] += 1
            else:
                if cache[nx][ny]:
                    failed = True
                    break
                cache[nx][ny] += 1
                x,y = nx,ny
                time += 1
        else:
            x,y = nx,ny
            time += 1
    else:
        d = (d-1)%4
        nx,ny = x+dx[d],y+dy[d]
        if cache[nx][ny]:
            failed = True
            break
        cache[nx][ny] += 1
        x,y = nx,ny
        time += 1
    nx,ny = x+dx[d],y+dy[d]

print(time if not failed else -1)