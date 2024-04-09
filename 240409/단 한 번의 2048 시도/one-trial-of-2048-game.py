import sys

board = [list(map(int,sys.stdin.readline().split())) for _ in range(4)]
direction = sys.stdin.readline().strip()

if direction == 'L':
    for row in range(4):
        temp = [0]*4
        idx = 0
        for col in range(4):
            if board[row][col] != 0:
                temp[idx] = board[row][col]
                board[row][col] = 0
                idx += 1
        for i in range(3):
            if temp[i] == temp[i+1]:
                temp[i] += temp[i+1]
                temp[i+1] = 0
        col = 0
        for i in range(4):
            if temp[i] != 0:
                board[row][col] = temp[i]
                col += 1
elif direction == 'R':
    for row in range(4):
        temp = [0]*4
        idx = 3
        for col in range(3,-1,-1):
            if board[row][col] != 0:
                temp[idx] = board[row][col]
                board[row][col] = 0
                idx -= 1
        for i in range(3,0,-1):
            if temp[i] == temp[i-1]:
                temp[i] += temp[i-1]
                temp[i-1] = 0
        col = 3
        for i in range(3,-1,-1):
            if temp[i] != 0:
                board[row][col] = temp[i]
                col -= 1
elif direction == 'U':
    for col in range(4):
        temp = [0]*4
        idx = 0
        for row in range(4):
            if board[row][col] != 0:
                temp[idx] = board[row][col]
                board[row][col] = 0
                idx += 1
        for i in range(3):
            if temp[i] == temp[i+1]:
                temp[i] += temp[i+1]
                temp[i+1] = 0
        row = 0
        for i in range(4):
            if temp[i] != 0:
                board[row][col] = temp[i]
                row += 1
else:
    for col in range(4):
        temp = [0]*4
        idx = 3
        for row in range(3,-1,-1):
            if board[row][col] != 0:
                temp[idx] = board[row][col]
                board[row][col] = 0
                idx -= 1
        for i in range(3,0,-1):
            if temp[i] == temp[i-1]:
                temp[i] += temp[i-1]
                temp[i-1] = 0
        row = 3
        for i in range(3,-1,-1):
            if temp[i] != 0:
                board[row][col] = temp[i]
                row -= 1

for line in board: print(*line)