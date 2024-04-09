import sys

n, r, c = map(int,sys.stdin.readline().split())
r,c = r-1,c-1
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = []
while True:
    move = False
    th = board[r][c]
    visited.append(th)
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] > th:
                r,c = nr,nc
                move = True
                break
    if not move: break

print(*visited)