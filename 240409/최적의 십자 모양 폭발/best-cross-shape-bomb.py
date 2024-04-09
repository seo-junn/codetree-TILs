import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def fall(board):
    for col in range(n):
        temp = [0]*n
        idx = n-1
        for row in range(n-1,-1,-1):
            if board[row][col]:
                temp[idx] = board[row][col]
                idx -= 1
        for row in range(n):
            board[row][col] = temp[row]

def check(board):
    count = 0
    for row in range(n):
        for col in range(n-1):
            if board[row][col] != 0 and board[row][col] == board[row][col+1]:
                count += 1
    for col in range(n):
        for row in range(n-1):
            if board[row][col] != 0 and board[row][col] == board[row+1][col]:
                count += 1
    
    return count

def explosion(br,bc,board):
    temp_board = [[0]*n for _ in range(n)]
    length = board[br][bc]
    for row in range(n):
        for col in range(n):
            if not((row == br and abs(col-bc) < length) or (col == bc and abs(row-br) < length)):
                temp_board[row][col] = board[row][col]

    fall(temp_board)
    return check(temp_board)

max_count = 0
for r in range(n):
    for c in range(n):
        max_count = max(max_count,explosion(r,c,board))

print(max_count)