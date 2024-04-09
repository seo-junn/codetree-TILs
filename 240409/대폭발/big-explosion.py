import sys

n,m,r,c = map(int,sys.stdin.readline().split())
r,c = r-1,c-1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def set_bomb(board,dist):
    cache = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if board[row][col] and cache[row][col] == 0:
                cache[row][col] += 1
                for i in range(4):
                    nr,nc = row+dr[i]*dist,col+dc[i]*dist
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and cache[nr][nc] == 0:
                        cache[nr][nc] += 1
                        board[nr][nc] += 1

board = [[0]*n for _ in range(n)]
board[r][c] = 1
for i in range(m):
    dist = 2**i
    set_bomb(board,dist)

bomb_count = 0
for row in range(n):
    for col in range(n):
        bomb_count += board[row][col]

print(bomb_count)