n = int(input())
board = [['*']*n for _ in range(n)]

for row in range(1,n-1):
    for col in range(row,n-1):
        board[row][col] = ' '

for line in board: print(*line)