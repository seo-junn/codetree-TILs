import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [0, 1]
dc = [1, 0]

cache = [[0]*m for _ in range(n)]

def search(pr,pc):
    for i in range(2):
        nr, nc = pr+dr[i], pc+dc[i]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] and cache[nr][nc] == 0:
            cache[nr][nc] += 1
            search(nr,nc)

cache[0][0] += 1
search(0,0)
print(cache[-1][-1])