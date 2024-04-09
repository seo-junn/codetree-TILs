import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n,m,t = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

balls = deque()
pos = [[0]*n for _ in range(n)]
for _ in range(m):
    r,c = map(lambda x:int(x)-1,sys.stdin.readline().split())
    pos[r][c] = 1
    balls.append((r,c))

for _ in range(t):
    for pr,pc in balls:
        max_val = 0
        npr,npc = -1,-1
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] > max_val:
                    max_val = board[nr][nc]
                    npr,npc = nr,nc
        if npr != -1 and npc != -1:
            pos[pr][pc] -= 1
            pos[npr][npc] += 1
                    
    balls = deque()
    for row in range(n):
        for col in range(n):
            if pos[row][col] == 1:
                balls.append((row,col))
            else:
                pos[row][col] = 0

print(len(balls))