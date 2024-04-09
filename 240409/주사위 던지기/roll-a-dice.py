import sys

n,m,r,c = map(int,sys.stdin.readline().split())
r,c = r-1,c-1
board = [[0]*n for _ in range(n)]

top,front,right = 1,2,3
direc = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

def roll_dice(direction,dice):
    top,front,right = dice
    if direction == 'L':
        top,right = right,7-top
    elif direction == 'R':
        top,right = 7-right,top
    elif direction == 'U':
        top,front = front,7-top
    else:
        top,front = 7-front,top
    return (top,front,right)

board[r][c] = 7-top
for d in sys.stdin.readline().strip().split():
    dr,dc = direc[d]
    nr,nc = r+dr,c+dc
    if 0 <= nr < n and 0 <= nc < n:
        dice = (top,front,right)
        top,front,right = roll_dice(d,dice)
        board[nr][nc] = 7-top
        r,c = nr,nc

total_sum = 0
for row in range(n):
    for col in range(n):
        total_sum += board[row][col]

print(total_sum)