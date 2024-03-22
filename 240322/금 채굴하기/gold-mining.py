import sys
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        gold = board[i][j]
        q = deque()
        q.append((i,j))
        cache = [[0]*n for _ in range(n)]
        cache[i][j] += 1
        for depth in range(n+1):
            nq = deque()
            while q:
                pr,pc = q.popleft()
                if board[pr][pc]: gold += 1
                for i in range(4):
                    nr,nc = pr+dr[i],pc+dc[i]
                    if 0 <= nr < n and 0 <= nc < n and cache[nr][nc] == 0:
                        cache[nr][nc] += 1
                        nq.append((nr,nc))

            cost = depth**2 + (depth+1)**2
            if cost <= gold*m:
                ans = max(ans,gold)
            q = nq

print(ans)