import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]
d_mask = {'U':0,'R':1,'D':2,'L':3}

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    board = {}
    lb,ub = sys.maxsize, -sys.maxsize
    for i in range(1,N+1):
        x,y,w,d = sys.stdin.readline().strip().split()
        x,y,w = int(x)*2,int(y)*2,int(w)
        lb = min(lb,x,y)
        ub = max(ub,x,y)
        board[(x,y)] = (w,i,d_mask[d])
    
    last_colision_time = -1
    time = 0
    while board:
        time += 1
        next_board = {}
        colision = False
        for key in board.keys():
            px,py = key
            w,num,d = board[key]
            nx,ny = px+dx[d],py+dy[d]
            if lb <= nx <= ub and lb <= ny <= ub:
                n_key = (nx,ny)
                if n_key in next_board.keys():
                    colision = True
                    cw,cnum,cd = next_board[n_key]
                    if w > cw or (w == cw and num > cnum):
                        next_board[n_key] = (w,num,d)
                else:
                    next_board[n_key] = (w,num,d)
        if colision:
            last_colision_time = time
        board = next_board
    
    print(last_colision_time)