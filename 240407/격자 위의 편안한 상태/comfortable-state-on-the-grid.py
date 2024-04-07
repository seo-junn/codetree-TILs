import sys

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, M = map(int,sys.stdin.readline().split())
board = [[0]*N for _ in range(N)]

for _ in range(M):
    r,c = map(lambda x:int(x)-1,sys.stdin.readline().split())
    board[r][c] = 1
    cnt = 0
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
            cnt += 1
    print(1 if cnt == 3 else 0)