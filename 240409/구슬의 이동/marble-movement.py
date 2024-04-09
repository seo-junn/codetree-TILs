import sys
from collections import deque

chdir = {'U':'D','D':'U','L':'R','R':'L'}
direct = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

n,m,t,k = map(int,sys.stdin.readline().split())

def move(pr,pc,cd,v):
    cnt = 0
    while cnt < v:
        dr,dc = direct[cd]
        nr,nc = pr+dr,pc+dc
        if 0 <= nr < n and 0 <= nc < n:
            pr,pc = nr,nc
            cnt += 1
        else:
            cd = chdir[cd]
    return pr,pc,cd

class ball:
    def __init__(self,row,col,direction,velocity,ball_number):
        self.row = row
        self.col = col
        self.direction = direction
        self.velocity = velocity
        self.ball_number = ball_number
    
    def get_pos(self):
        return (self.row,self.col)

    def comp_info(self):
        return self.row,self.col,-self.velocity,-self.ball_number

    def get_info(self):
        return (self.row,self.col,self.direction,self.velocity)
    
    def update(self,n_row,n_col,n_direct):
        self.row = n_row
        self.col = n_col
        self.direction = n_direct
    
    def __str__(self):
        return "row : " + str(self.row) + "\tcol : " + str(self.col) + "\tdir : " + self.direction + \
              "\tvelocity : " + str(self.velocity) + "\tball number : " + str(self.ball_number)


balls = []
positions = [[0]*n for _ in range(n)]
for i in range(1,m+1):
    r,c,d,v = sys.stdin.readline().split()
    r,c,v = int(r)-1,int(c)-1,int(v)
    balls.append(ball(r,c,d,v,i))
    positions[r][c] += 1

for _ in range(t):
    for b in balls:
        pr,pc,d,v = b.get_info()
        nr,nc,nd = move(pr,pc,d,v)
        b.update(nr,nc,nd)
        positions[pr][pc] -= 1
        positions[nr][nc] += 1
    
    next_balls = []
    balls.sort(key=lambda x:tuple(x.comp_info()))
    target = ()
    count = 0
    for b in balls:
        if target == b.get_pos():
            if count < k:
                count += 1
                next_balls.append(b)
        else:
            target = b.get_pos()
            count = 1
            next_balls.append(b)

    balls = next_balls

print(len(balls))