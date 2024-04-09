import sys

N, M, K = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def fall():
    for col in range(N):
        temp = [0]*N
        idx = N-1
        for row in range(N-1,-1,-1):
            if board[row][col]:
                temp[idx] = board[row][col]
                idx -= 1
        for row in range(N):
            board[row][col] = temp[row]

def rotate(board):
    new_board = [[0]*N for _ in range(N)]
    for row in range(N-1,-1,-1):
        for col in range(N):
            new_board[col][N-1-row] = board[row][col]
    
    for row in range(N):
        for col in range(N):
            board[row][col] = new_board[row][col]

    fall()

def explosion():
    for col in range(N):
        temp = []
        target = 0
        count = 0
        for row in range(N-1,-1,-1):
            if board[row][col] != 0 and board[row][col] == target:
                count += 1
            else:
                if target != 0 and count < M:
                    temp += [target]*count
                target = board[row][col]
                count = 1
            board[row][col] = 0
        if target != 0 and count < M:
            temp += [target]*count
        for idx in range(len(temp)):
            board[row-1-idx][col] = temp[idx]

for _ in range(K):
    explosion()
    rotate(board)
explosion()

count = 0
for row in range(N):
    for col in range(N):
        if board[row][col] != 0: count += 1

print(count)