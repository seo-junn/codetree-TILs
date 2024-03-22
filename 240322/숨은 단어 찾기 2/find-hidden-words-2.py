import sys

N, M = map(int,sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]

dn = [0,0]
du = [1,2]
dl = [-1,-2]

def check(row,col,dr,dc):
    temp = 0
    for i in range(2):
        nr, nc = row+dr[i], col+dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 'E':
                temp += 1
    return True if temp == 2 else False

count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            if check(i,j,dl,dn): count += 1
            if check(i,j,dl,du): count += 1
            if check(i,j,dn,du): count += 1
            if check(i,j,du,du): count += 1
            if check(i,j,du,dn): count += 1
            if check(i,j,du,dl): count += 1
            if check(i,j,dn,dl): count += 1
            if check(i,j,dl,dl): count += 1

print(count)