import sys
from collections import deque
from itertools import combinations

n, k, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
start_points = [tuple(map(lambda x:int(x)-1,sys.stdin.readline().split())) for _ in range(k)]

stones = []
for row in range(n):
    for col in range(n):
        if board[row][col]:
            stones.append((row,col))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

max_count = 0
for taken in combinations(stones,m):
    # stone cleaning
    for r,c in taken: board[r][c] = 0
    # search
    q = deque()
    visited = [[False]*n for _ in range(n)]
    count = 0
    for r,c in start_points:
        visited[r][c] = True
        q.append((r,c))
        count += 1
    
    while q:
        pr,pc = q.popleft()
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))
                count += 1
    
    # stone recovering
    for r,c in taken: board[r][c] = 1

    max_count = max(max_count,count)

    

print(max_count)