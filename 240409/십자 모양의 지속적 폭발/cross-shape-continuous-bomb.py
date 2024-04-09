import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def fall():
    for col in range(n):
        temp = [0]*n
        idx = n-1
        for row in range(n-1,-1,-1):
            if board[row][col]:
                temp[idx] = board[row][col]
                idx -= 1
        for row in range(n):
            board[row][col] = temp[row]

def bomb(br,bc):
    length = board[br][bc]
    board[br][bc] = 0
    for i in range(1,length):
        nr,nc = br-i,bc
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] = 0
        nr,nc = br,bc+i
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] = 0
        nr,nc = br+i,bc
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] = 0
        nr,nc = br,bc-i
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] = 0
    fall()

for _ in range(m):
    col = int(sys.stdin.readline())-1
    ex_bomb = False
    for row in range(n):
        if board[row][col]:
            ex_bomb = True
            br,bc = row,col
            break
    if ex_bomb: bomb(br,bc)

for line in board: print(*line)