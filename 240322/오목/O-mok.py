import sys

board = [list(map(int,sys.stdin.readline().split())) for _ in range(19)]
D = [-2,-1,0,1,2]

def check(row,col,color):
    count = 0
    for d in D:
        nr = row + d
        if 0 <= nr < 19:
            if board[nr][col] == color:
                count += 1
    if count == 5: return True

    count = 0
    for d in D:
        nc = col + d
        if 0 <= nc < 19:
            if board[row][nc] == color:
                count += 1
    if count == 5: return True

    count = 0
    for d in D:
        nr, nc = row+d,col+d
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == color:
                count += 1
    if count == 5: return True

    count = 0
    for d in D:
        nr, nc = row+d,col-d
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == color:
                count += 1
    if count == 5: return True

    return False

find = False
for i in range(19):
    for j in range(19):
        if board[i][j]:
            if check(i,j,board[i][j]):
                who = board[i][j]
                row, col = i+1, j+1
                find = True

if find:
    print(who)
    print(row,col)
else:
    print(0)