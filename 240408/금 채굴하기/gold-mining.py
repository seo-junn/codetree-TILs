import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def search(row,col,max_depth):
    q = deque()
    q.append((row,col))
    cache = [[0]*n for _ in range(n)]
    cache[row][col] += 1
    gold = 0
    ans = 0
    for depth in range(max_depth):
        nq = deque()
        while q:
            pr,pc = q.popleft()
            if board[pr][pc]: gold += 1
            for i in range(4):
                nr,nc = pr+dr[i],pc+dc[i]
                if 0 <= nr < n and 0 <= nc < n and cache[nr][nc] == 0:
                    cache[nr][nc] += 1
                    nq.append((nr,nc))
        q = nq
        if depth*depth + (depth+1)*(depth+1) <= gold*m: ans = gold
    return ans

res = 0
for row in range(n):
    for col in range(n):
        res = max(res,search(row,col,n))

print(res)