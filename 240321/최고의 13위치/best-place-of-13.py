import sys

N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

max_coin = 0
for i in range(N):
    for j in range(N-2):
        max_coin = max(max_coin,board[i][j]+board[i][j+1]+board[i][j+2])

print(max_coin)