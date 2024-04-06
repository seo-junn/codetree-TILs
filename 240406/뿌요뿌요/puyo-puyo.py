import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[False]*n for _ in range(n)]
def dfs(pr,pc,target):
    count = 0
    for i in range(4):
        nr, nc = pr+dr[i], pc+dc[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == target and not visited[nr][nc]:
            visited[nr][nc] = True
            count += 1 + dfs(nr,nc,target)
    return count

max_block_count = 0
num_bomb = 0
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            visited[row][col] = True
            current_count = 1 + dfs(row,col,board[row][col])
            if current_count >= 4: num_bomb += 1
            max_block_count = max(max_block_count,current_count)

print(num_bomb, max_block_count)