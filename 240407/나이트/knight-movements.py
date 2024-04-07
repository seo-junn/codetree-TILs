import sys
from collections import deque

n = int(sys.stdin.readline())
cache = [[-1]*n for _ in range(n)]
sr,sc,er,ec = map(lambda x:int(x)-1,sys.stdin.readline().split())

dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

q = deque()
q.append((sr,sc))
cache[sr][sc] = 0

while q:
    pr,pc = q.popleft()
    if pr == er and pc == ec: break
    for i in range(8):
        nr,nc = pr+dr[i],pc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and cache[nr][nc] == -1:
            cache[nr][nc] = cache[pr][pc] + 1
            q.append((nr,nc))

print(cache[er][ec])