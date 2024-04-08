import sys

N, M, Q = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dr = [-1,0,1,0,0]
dc = [0,1,0,-1,0]

def wind(r1,c1,r2,c2):
    temp = board[r1][c2]
    for i in range(c2,c1,-1):
        board[r1][i] = board[r1][i-1]
    for i in range(r1,r2):
        board[i][c1] = board[i+1][c1]
    for i in range(c1,c2):
        board[r2][i] = board[r2][i+1]
    for i in range(r2,r1+1,-1):
        board[i][c2] = board[i-1][c2]
    board[r1+1][c2] = temp

    temp = [[0]*(c2-c1+1) for _ in range(r1,r2+1)]

    for row in range(r1,r2+1):
        for col in range(c1,c2+1):
            count = 0
            total = 0
            for i in range(5):
                r,c = row+dr[i],col+dc[i]
                if 0 <= r < N and 0 <= c < M:
                    count += 1
                    total += board[r][c]
            temp[row-r1][col-c1] = total//count
    
    for row in range(r1,r2+1):
        for col in range(c1,c2+1):
            board[row][col] = temp[row-r1][col-c1]

for _ in range(Q):
    r1,c1,r2,c2 = map(lambda x:int(x)-1,sys.stdin.readline().split())
    wind(r1,c1,r2,c2)

for line in board: print(*line)