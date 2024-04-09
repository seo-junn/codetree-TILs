import sys

dir_map = {'U':0,'R':1,'D':2,'L':3}
dr = [-1,0,1,0]
dc = [0,1,0,-1]

n, m, t = map(int,sys.stdin.readline().split())
board = [[[] for __ in range(n)] for _ in range(n)]

for i in range(1,m+1):
    r,c,d,w = sys.stdin.readline().split()
    r,c,d,w = int(r)-1,int(c)-1,dir_map[d],int(w)
    board[r][c].append((i,d,w))

for _ in range(t):
    new_board = [[[] for __ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if board[row][col]:
                i,d,w = board[row][col][0]
                nr,nc = row+dr[d],col+dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    new_board[nr][nc].append((i,d,w))
                else:
                    d = (d+2)%4
                    new_board[row][col].append((i,d,w))
    for row in range(n):
        for col in range(n):
            if len(new_board[row][col]) > 1:
                new_board[row][col].sort(key=lambda x:-x[0])
                ni = new_board[row][col][0][0]
                nd = new_board[row][col][0][1]
                weight = 0
                for i in range(len(new_board[row][col])):
                    weight += new_board[row][col][i][2]
                new_board[row][col] = [(ni,nd,weight)]
    
    board = new_board

count = 0
max_weight = 0
for row in range(n):
    for col in range(n):
        if board[row][col]:
            count += 1
            max_weight = max(max_weight,board[row][col][0][-1])

print(count,max_weight)