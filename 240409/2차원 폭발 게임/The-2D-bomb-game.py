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
        for row in range(N):
            if board[row][col]:
                temp.append(board[row][col])
                board[row][col] = 0
        
        while True:
            exploded = False
            target = 0
            count = 0
            next_temp = []
            for i in range(len(temp)):
                if temp[i] == target:
                    count += 1
                else:
                    if count < M:
                        next_temp += [target]*count
                    else:
                        exploded = True
                    target = temp[i]
                    count = 1
            if count < M:
                next_temp += [target]*count
            else:
                exploded = True
            
            if not exploded: break
            temp = next_temp
        
        row = N-1
        for idx in range(len(temp)-1,-1,-1):
            board[row][col] = temp[idx]
            row -= 1

for _ in range(K):
    explosion()
    rotate(board)
explosion()

count = 0
for row in range(N):
    for col in range(N):
        if board[row][col] != 0: count += 1

print(count)