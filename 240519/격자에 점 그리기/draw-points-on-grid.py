n,m = map(int,input().split())

board = [[0]*n for _ in range(n)]

for i in range(1,m+1):
    r,c = map(lambda x:int(x)-1,input().split())
    board[r][c] = i

for line in board: print(*line)