import sys

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
K = int(sys.stdin.readline())

dr = [1,0,-1,0]
dc = [0,-1,0,1]

chdir1 = {0:1,1:0,2:3,3:2}
chdir2 = {0:3,3:0,1:2,2:1}

c_dir = (K-1)//N
if c_dir == 0:
    pr,pc = -1,(K-1)%N
elif c_dir == 1:
    pr,pc = (K-1)%N,N
elif c_dir == 2:
    pr,pc = N,N-1-(K-1)%N
else:
    pr,pc = N-1-(K-1)%N,-1

count = 0
while True:
    nr,nc = pr+dr[c_dir],pc+dc[c_dir]
    if 0 <= nr < N and 0 <= nc < N:
        if board[nr][nc] == '/':
            c_dir = chdir1[c_dir]
        else:
            c_dir = chdir2[c_dir]
        count += 1
        pr,pc = nr,nc
    else:
        break

print(count)