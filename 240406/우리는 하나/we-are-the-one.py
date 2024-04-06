import sys
from collections import deque
from itertools import combinations
from itertools import product

n, k, u, d = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

base = product(range(n),repeat=2)
max_count = 0
for taken in combinations(base,k):
    q = deque()
    count = 0
    visited = [[False]*n for _ in range(n)]
    for r,c in taken:
        visited[r][c] = True
        q.append((r,c))
        count += 1
    
    while q:
        pr,pc = q.popleft()
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n and u <= abs(board[pr][pc]-board[nr][nc]) <= d and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))
                count += 1
    
    max_count = max(max_count,count)

print(max_count)