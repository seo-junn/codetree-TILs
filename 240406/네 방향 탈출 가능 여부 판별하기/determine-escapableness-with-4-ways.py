import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
q = deque()
visited[0][0] = 1
q.append((0,0))

while q:
    pr,pc = q.popleft()
    for i in range(4):
        nr, nc = pr+dr[i], pc+dc[i]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] += 1
            q.append((nr,nc))

print(visited[-1][-1])