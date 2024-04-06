import sys

N, M = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def search(pr,pc):
    for i in range(4):
        nr, nc = pr+dr[i], pc+dc[i]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > K and visited[nr][nc] == 0:
            visited[nr][nc] += 1
            search(nr,nc)

max_count = 0
target = 0
for K in range(1,101):
    visited = [[0]*M for _ in range(N)]
    count = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] > K and visited[row][col] == 0:
                count += 1
                visited[row][col] += 1
                search(row,col)
    if count == 0: break
    if max_count < count:
        max_count = count
        target = K

print(target,max_count)