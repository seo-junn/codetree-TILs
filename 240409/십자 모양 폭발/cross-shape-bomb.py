import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
r,c = map(lambda x:int(x)-1,sys.stdin.readline().split())

length = board[r][c]
board[r][c] = 0
for i in range(1,length):
    nr,nc = r-i,c
    if 0 <= nr < n and 0 <= nc < n:
        board[nr][nc] = 0
    nr,nc = r,c+i
    if 0 <= nr < n and 0 <= nc < n:
        board[nr][nc] = 0
    nr,nc = r+i,c
    if 0 <= nr < n and 0 <= nc < n:
        board[nr][nc] = 0
    nr,nc = r,c-i
    if 0 <= nr < n and 0 <= nc < n:
        board[nr][nc] = 0

for col in range(n):
    temp = [0]*n
    idx = n-1
    for row in range(n-1,-1,-1):
        if board[row][col] != 0:
            temp[idx] = board[row][col]
            idx -= 1
    for row in range(n):
        board[row][col] = temp[row]

for line in board: print(*line)