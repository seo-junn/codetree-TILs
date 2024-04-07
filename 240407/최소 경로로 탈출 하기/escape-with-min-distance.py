import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

cache = [[-1]*m for _ in range(n)]
q = deque()
cache[0][0] = 0
q.append((0,0))

while q:
    pr,pc = q.popleft()
    for i in range(4):
        nr,nc = pr+dr[i],pc+dc[i]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] and cache[nr][nc] == -1:
            cache[nr][nc] = cache[pr][pc] + 1
            q.append((nr,nc))

print(cache[-1][-1])