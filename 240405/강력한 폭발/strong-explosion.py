import sys
import copy

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

bomb1 = [(-2,0),(-1,0),(0,0),(1,0),(2,0)]
bomb2 = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]
bomb3 = [(-1,-1),(-1,1),(1,-1),(1,1),(0,0)]
bomb_dxy = [bomb1, bomb2, bomb3]

bomb_pos = []
for i in range(n):
    for j in range(n):
        if board[i][j]:
            bomb_pos.append((i,j))
num_bomb = len(bomb_pos)

max_score = 0
def check(board,comb):
    global max_score
    temp_board = copy.deepcopy(board)
    for i in range(num_bomb):
        px,py = bomb_pos[i]
        for j in range(5):
            dx,dy = bomb_dxy[comb[i]][j]
            nx,ny = px+dx, py+dy
            if 0 <= nx < n and 0 <= ny < n and temp_board[nx][ny] == 0:
                temp_board[nx][ny] += 1
    score = 0
    for i in range(n):
        for j in range(n):
            score += temp_board[i][j]
    max_score = max(max_score,score)

comb = []
def make_cases(depth):
    if depth == 0:
        check(board,comb)
        return
    for i in range(3):
        comb.append(i)
        make_cases(depth-1)
        comb.pop()

make_cases(num_bomb)

print(max_score)