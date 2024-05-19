n,m = map(int,input().split())

board = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c = map(lambda x:int(x)-1,input().split())
    board[r][c] = 1

for line in board: print(*line)