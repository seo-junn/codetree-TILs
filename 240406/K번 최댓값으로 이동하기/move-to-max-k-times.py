import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
row, col = map(int,sys.stdin.readline().split())
row -= 1
col -= 1

dr = [-1,0,0,1]
dc = [0,-1,1,0]

while k > 0:
    k -= 1
    visited = [[False]*n for _ in range(n)]
    max_val = 0
    candidates = []
    q = deque()
    q.append((row,col))
    visited[row][col] = True
    threshold = board[row][col]
    
    while q:
        pr,pc = q.popleft()
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] < threshold and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))
                val = board[nr][nc]
                if val > max_val:
                    max_val = val
                    candidates = [(nr,nc)]
                elif val == max_val:
                    candidates.append((nr,nc))
    
    candidates.sort()
    if candidates:
        row,col = candidates[0]
    else:
        break

print(row+1,col+1)