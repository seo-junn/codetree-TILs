import sys

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def swap(pr,pc):
    val = 0
    tr,tc = -1,-1
    for i in range(8):
        nr,nc = pr+dr[i],pc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and val < board[nr][nc]:
            val = board[nr][nc]
            tr,tc = nr,nc
    board[pr][pc],board[tr][tc] = board[tr][tc],board[pr][pc]

def turn():
    for target in range(1,n*n+1):
        done = False
        for row in range(n):
            for col in range(n):
                if board[row][col] == target:
                    swap(row,col)
                    done = True
                    break
            if done: break

for _ in range(m): turn()

for line in board: print(*line)