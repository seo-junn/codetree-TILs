import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[0]*n for _ in range(n)]

def search(pr,pc):
    current_count = 0
    for i in range(4):
        nr, nc = pr+dr[i], pc+dc[i]
        if 0 <= nr <n and 0 <= nc < n and board[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] += 1
            current_count += 1 + search(nr,nc)
    return current_count

population = []
town = 0
for row in range(n):
    for col in range(n):
        if board[row][col] and visited[row][col] == 0:
            town += 1
            visited[row][col] += 1
            population.append(search(row,col)+1)

population.sort()
print(town)
for item in population: print(item)