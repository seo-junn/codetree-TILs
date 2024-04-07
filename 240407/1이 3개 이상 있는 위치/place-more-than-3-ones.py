import sys

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

res = 0
for row in range(n):
    for col in range(n):
        count = 0
        for i in range(4):
            nr,nc = row+dr[i],col+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc]:
                count += 1
        if count >= 3: res += 1

print(res)