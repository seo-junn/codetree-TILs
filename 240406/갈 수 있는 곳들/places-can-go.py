import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
q = deque()

for _ in range(k):
    r,c = map(int,sys.stdin.readline().split())
    visited[r-1][c-1] = True
    q.append((r-1,c-1))

while q:
    pr,pc = q.popleft()
    for i in range(4):
        nr,nc = pr+dr[i],pc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr,nc))

count = 0
for row in range(n):
    for col in range(n):
        if visited[row][col]: count += 1

print(count)