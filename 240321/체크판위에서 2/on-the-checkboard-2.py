import sys

R, C = map(int,sys.stdin.readline().split())
board = [sys.stdin.readline().strip().split() for _ in range(R)]

color = {'W':'B','B':'W'}
now = board[0][0]

count = 0
for row in range(1,R):
    for col in range(1,C):
        if board[row][col] == color[now]:
            for r in range(row+1,R-1):
                for c in range(col+1,C-1):
                    if board[r][c] == now:
                        count += 1

print(count)