import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
board = [list(map(lambda x:deque([int(x)]),sys.stdin.readline().split())) for _ in range(n)]
targets = list(map(int,sys.stdin.readline().split()))

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

for target in targets:
    tr,tc,tidx = -1,-1,-1
    find = False
    for row in range(n):
        for col in range(n):
            if target in board[row][col]:
                tr,tc = row,col
                for i in range(len(board[row][col])):
                    if board[row][col][i] == target:
                        tidx = i
                        break
                find = True
                break
        if find: break
    
    val = 0
    npr,npc = -1,-1
    for i in range(8):
        nr,nc = tr+dr[i],tc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and len(board[nr][nc]):
            if max(board[nr][nc]) > val:
                val = max(board[nr][nc])
                npr,npc = nr,nc
    if npr == -1 and npc == -1: continue

    temp = deque()
    for i in range(tidx+1):
        temp.append(board[tr][tc].popleft())

    for i in range(tidx+1):
        board[npr][npc].appendleft(temp.pop())

for row in range(n):
    for col in range(n):
        if board[row][col]:
            print(*board[row][col])
        else:
            print("None")