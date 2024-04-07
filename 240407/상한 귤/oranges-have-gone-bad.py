import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

wasted = []
for row in range(n):
    for col in range(n):
        if board[row][col] == 2:
            wasted.append((row,col))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

q = deque()
cache = [[-2]*n for _ in range(n)]
for r,c in wasted:
    q.append((r,c))
    cache[r][c] = 0

while q:
    pr,pc = q.popleft()
    for i in range(4):
        nr,nc = pr+dr[i],pc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 1 and cache[nr][nc] == -2:
            cache[nr][nc] = cache[pr][pc]+1
            q.append((nr,nc))

ans = [[-1]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if board[row][col]:
            ans[row][col] = cache[row][col]

for line in ans: print(*line)