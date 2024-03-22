import sys

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def search(row, col, depth, cache):
    if row < 0 or row >= n or col < 0 or col >= m: return -1000
    if cache[row][col]: return -1000
    if depth == 0:
        cache[row][col] += 1
        return board[row][col]
    cache[row][col] += 1
    res = board[row][col] + max(search(row-1,col,depth-1,cache),search(row+1,col,depth-1,cache),search(row,col+1,depth-1,cache),search(row,col-1,depth-1,cache))
    return res

ans = 0
for i in range(n):
    for j in range(m):
        cache = [[0]*m for _ in range(n)]
        ans = max(ans,search(i,j,2,cache))

print(ans)