import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

ch_dir1 = {0:1,1:0,2:3,3:2}
ch_dir2 = {0:3,1:2,2:1,3:0}

def game(sr,sc,d):
    time = 0
    pr,pc = sr,sc
    while True:
        nr,nc = pr+dr[d],pc+dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 1:
                d = ch_dir1[d]
            elif board[nr][nc] == 2:
                d = ch_dir2[d]
            pr,pc = nr,nc
            time += 1
        else:
            time += 1
            break
    return time

max_game_time = 0
for i in range(n):
    max_game_time = max(max_game_time,game(-1,i,2))
for i in range(n):
    max_game_time = max(max_game_time,game(i,n,3))
for i in range(n):
    max_game_time = max(max_game_time,game(n,i,0))
for i in range(n):
    max_game_time = max(max_game_time,game(i,-1,1))

print(max_game_time)