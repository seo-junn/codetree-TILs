import sys
from collections import deque

direct = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
chdir = {'U':'D','D':'U','L':'R','R':'L'}

for _ in range(int(sys.stdin.readline())):
    N,M = map(int,sys.stdin.readline().split())
    balls = []
    pos = [[0]*N for _ in range(N)]
    for _ in range(M):
        r,c,d = sys.stdin.readline().strip().split()
        r,c = int(r)-1,int(c)-1
        pos[r][c] += 1
        balls.append((r,c,d))
    
    for _ in range(2*N):
        next_balls = []
        for pr,pc,d in balls:
            dr,dc = direct[d]
            nr,nc = pr+dr,pc+dc
            if 0 <= nr < N and 0 <= nc < N:
                pos[pr][pc] -= 1
                pos[nr][nc] += 1
                next_balls.append((nr,nc,d))
            else:
                d = chdir[d]
                next_balls.append((pr,pc,d))
        
        balls = []
        for pr,pc,d in next_balls:
            if pos[pr][pc] == 1:
                balls.append((pr,pc,d))
        for row in range(N):
            for col in range(N):
                if pos[row][col] != 1:
                    pos[row][col] = 0
    
    print(len(balls))