import sys
from collections import deque
from itertools import combinations

n, k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sr,sc = map(lambda x:int(x)-1,sys.stdin.readline().split())
er,ec = map(lambda x:int(x)-1,sys.stdin.readline().split())
cache = [[-1]*n for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

walls = []
for row in range(n):
    for col in range(n):
        if board[row][col]:
            walls.append((row,col))

min_time = sys.maxsize
for taken in combinations(walls,k):
    # remove wall
    for r,c in taken:
        board[r][c] = 0
    
    q = deque()
    cache = [[-1]*n for _ in range(n)]
    q.append((sr,sc))
    cache[sr][sc] = 0

    while q:
        pr,pc = q.popleft()
        if pr == er and pc == ec: break
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and cache[nr][nc] == -1:
                cache[nr][nc] = cache[pr][pc] + 1
                q.append((nr,nc))
    
    # recover wall
    for r,c in taken:
        board[r][c] = 1

    if cache[er][ec] != -1:
        min_time = min(min_time,cache[er][ec])

print(min_time if min_time != sys.maxsize else -1)