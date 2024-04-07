import sys
from collections import deque

n, h, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc):
    q = deque()
    cache = [[-1]*n for _ in range(n)]
    q.append((sr,sc))
    cache[sr][sc] = 0

    while q:
        pr,pc = q.popleft()
        for i in range(4):
            nr, nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 and cache[nr][nc] == -1:
                cache[nr][nc] = cache[pr][pc] + 1
                q.append((nr,nc))
                if board[nr][nc] == 3:
                    return cache[nr][nc]
    
    return -1

ans = [[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if board[row][col] == 2:
            ans[row][col] = bfs(row,col)

for line in ans: print(*line)