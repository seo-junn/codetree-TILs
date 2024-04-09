import sys

n,m,k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
k -= 1

def check(row):
    for col in range(k,k+m):
        if board[row][col]:
            return False
    return True

row = 0
while check(row): row += 1
row -= 1

for col in range(k,k+m):
    board[row][col] = 1

for line in board: print(*line)