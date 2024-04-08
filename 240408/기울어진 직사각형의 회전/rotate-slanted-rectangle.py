import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
r,c,m1,m2,m3,m4,direction = map(int,sys.stdin.readline().split())
r,c = r-1,c-1

if direction == 0:
    temp = board[r][c]
    pr,pc = r,c
    for i in range(m4):
        nr,nc = pr-1,pc-1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m3):
        nr,nc = pr-1,pc+1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m2):
        nr,nc = pr+1,pc+1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m1-1):
        nr,nc = pr+1,pc-1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    board[pr][pc] = temp
else:
    temp = board[r][c]
    pr,pc = r,c
    for i in range(m1):
        nr,nc = pr-1,pc+1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m2):
        nr,nc = pr-1,pc-1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m3):
        nr,nc = pr+1,pc-1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    for i in range(m4-1):
        nr,nc = pr+1,pc+1
        board[pr][pc] = board[nr][nc]
        pr,pc = nr,nc
    board[pr][pc] = temp

for line in board: print(*line)