import sys
from collections import deque

N, M, K = map(int,sys.stdin.readline().split())
board = [[0]*N for _ in range(N)]

# apple
for _ in range(M):
    r,c = map(lambda x:int(x)-1,sys.stdin.readline().split())
    board[r][c] = 2

time = 0
snake = deque()
snake.append((0,0))
board[0][0] = 1
direct = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
Game = True

while K > 0 and Game:
    d, length = sys.stdin.readline().strip().split()
    K -= 1
    length = int(length)
    for _ in range(length):
        time += 1
        pr,pc = snake[0]
        dr,dc = direct[d]
        nr,nc = pr+dr,pc+dc
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == 2:
                snake.appendleft((nr,nc))
                board[nr][nc] = 1
            else:
                tr,tc = snake.pop()
                board[tr][tc] = 0
                if board[nr][nc] == 0:
                    snake.appendleft((nr,nc))
                    board[nr][nc] = 1
                else:
                    Game = False
                    break
        else:
            Game = False
            break

print(time)