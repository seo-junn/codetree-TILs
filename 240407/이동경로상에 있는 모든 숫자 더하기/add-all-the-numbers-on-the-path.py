import sys

N, T = map(int,sys.stdin.readline().split())
command = list(sys.stdin.readline().strip())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

pr,pc = N//2,N//2

dr = [-1,0,1,0]
dc = [0,1,0,-1]
c_dir = 0

total_sum = 0
total_sum += board[pr][pc]

for c in command:
    if c == 'L':
        c_dir = (c_dir-1)%4
    elif c == 'R':
        c_dir = (c_dir+1)%4
    else:
        nr,nc = pr+dr[c_dir],pc+dc[c_dir]
        if 0 <= nr < N and 0 <= nc < N:
            pr,pc = nr,nc
            total_sum += board[pr][pc]

print(total_sum)