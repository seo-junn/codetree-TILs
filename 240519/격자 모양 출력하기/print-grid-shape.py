n,m = map(int,input().split())

board = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c = map(int,input().split())
    board[r-1][c-1] = r*c

for line in board: print(*line)