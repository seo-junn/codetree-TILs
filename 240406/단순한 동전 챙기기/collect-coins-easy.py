import sys

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
coins = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 'S':
            sr,sc = r,c
        elif board[r][c] == 'E':
            er,ec = r,c
        elif board[r][c] != '.':
            coins.append((r,c,int(board[r][c])))

if len(coins) < 3:
    print(-1)
    exit(0)

coins.sort(key=lambda x:x[-1])

min_dist = sys.maxsize
def choose(curr_idx,coin_cnt,dist,px,py):
    if curr_idx == len(coins):
        if coin_cnt == 3:
            global min_dist
            min_dist = min(min_dist,dist+(abs(px-er)+abs(py-ec)))
        return
    
    choose(curr_idx+1,coin_cnt+1,dist+(abs(px-coins[curr_idx][0])+abs(py-coins[curr_idx][1])),coins[curr_idx][0],coins[curr_idx][1])

    choose(curr_idx+1,coin_cnt,dist,px,py)


choose(0,0,0,sr,sc)

print(min_dist)