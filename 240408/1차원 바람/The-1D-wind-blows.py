import sys
from collections import deque

N, M, Q = map(int,sys.stdin.readline().split())
board = [deque(map(int,sys.stdin.readline().split())) for _ in range(N)]
direction = {'L':'R','R':'L'}

def wind(r,d):
    ul = r-1
    ulb = r
    ud = direction[d]
    ll = r+1
    llb = r
    ld = direction[d]

    if d == 'L': board[r].appendleft(board[r].pop())
    else: board[r].append(board[r].popleft())

    while ul >= 0:
        flow = False
        for i in range(M):
            if board[ul][i] == board[ulb][i]:
                flow = True
                break
        if flow:
            if ud == 'L': board[ul].appendleft(board[ul].pop())
            else: board[ul].append(board[ul].popleft())
            ul -= 1
            ulb -= 1
            ud = direction[ud]
        else:
            break
    
    while ll < N:
        flow = False
        for i in range(M):
            if board[ll][i] == board[llb][i]:
                flow = True
                break
        if flow:
            if ld == 'L': board[ll].appendleft(board[ll].pop())
            else: board[ll].append(board[ll].popleft())
            ll += 1
            llb += 1
            ld = direction[ld]
        else:
            break

for _ in range(Q):
    r,d = sys.stdin.readline().strip().split()
    wind(int(r)-1,d)

for line in board: print(*line)