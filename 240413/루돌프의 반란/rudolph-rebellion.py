import sys
from collections import deque

N, M, P, C, D = map(int,sys.stdin.readline().split())

class Santa:
    def __init__(self,number,row,col,stun=0):
        self.number = number
        self.row = row
        self.col = col
        self.stun = stun

ru_dr = [-1,-1,0,1,1,1,0,-1]
ru_dc = [0,1,1,1,0,-1,-1,-1]
sa_dr = [-1,0,1,0]
sa_dc = [0,1,0,-1]

def rudolph_move(rr,rc):
    dist = sys.maxsize
    tr,tc = -1,-1
    # find nearest santa
    for santa in alived.values():
        sr,sc = santa.row, santa.col
        temp_dist = (rr-sr)**2+(rc-sc)**2
        if temp_dist < dist:
            tr,tc = sr,sc
            dist = temp_dist
        elif temp_dist == dist:
            if sr > tr or (sr == tr and sc > tc):
                tr,tc = sr,sc

    # find nearest direction
    dist = sys.maxsize
    dr,dc = 0,0
    for i in range(8):
        nr,nc = rr+ru_dr[i],rc+ru_dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            temp_dist = (nr-tr)**2+(nc-tc)**2
            if temp_dist < dist:
                dist = temp_dist
                dr,dc = ru_dr[i],ru_dc[i]

    # move
    nrr,nrc = rr+dr,rc+dc
    if board[nrr][nrc]:
        # when rudolph hit santa
        board[nrr][nrc].append(board[rr][rc].popleft())
        rudolph_hit(nrr,nrc,dr,dc)
    else:
        # when rudolph just move
        board[nrr][nrc].append(board[rr][rc].popleft())

    return nrr,nrc

def santa_move(santa_num,rr,rc):
    present_santa = alived[santa_num]
    # when santa was stunned
    if present_santa.stun:
        present_santa.stun -= 1
        return

    # find direction
    psr,psc = present_santa.row, present_santa.col
    sdr,sdc = 0,0
    dist = (psr-rr)**2 + (psc-rc)**2
    for i in range(4):
        nsr,nsc = psr+sa_dr[i], psc+sa_dc[i]
        if 0 <= nsr < N and 0 <= nsc < N:
            if (nsr == rr and nsc == rc) or len(board[nsr][nsc]) == 0:
                temp_dist = (nsr-rr)**2 + (nsc-rc)**2
                if temp_dist < dist:
                    dist = temp_dist
                    sdr,sdc = sa_dr[i], sa_dc[i]

    # when santa don't move
    if sdr == 0 and sdc == 0: return

    # move santa
    nsr,nsc = psr+sdr,psc+sdc
    present_santa.row = nsr
    present_santa.col = nsc
    # when santa hit the rudolph
    if board[nsr][nsc]:
        board[nsr][nsc].append(board[psr][psc].popleft())
        santa_hit(nsr,nsc,sdr,sdc)
    else:
        board[nsr][nsc].append(board[psr][psc].popleft())

def rudolph_hit(rr,rc,rdr,rdc):
    santa_num = board[rr][rc].popleft()
    present_santa = alived[santa_num]

    # santa get scored
    score_board[santa_num] += C

    # santa get stunned
    if present_santa.stun:
        present_santa.stun += 1
    else:
        present_santa.stun += 2

    # santa moved
    psr,psc = rr,rc
    nsr,nsc = psr+rdr*C,psc+rdc*C
    present_santa.row = nsr
    present_santa.col = nsc
    # when next destination is in range
    if 0 <= nsr < N and 0 <= nsc < N:
        # when there is another santa
        if board[nsr][nsc]:
            board[nsr][nsc].append(santa_num)
            splash(nsr,nsc,rdr,rdc)
        # when there is nothing
        else:
            board[nsr][nsc].append(santa_num)
    # when santa become out of range
    else:
        alived.pop(santa_num)

def santa_hit(pr,pc,sdr,sdc):
    santa_num = board[pr][pc].pop()
    present_santa = alived[santa_num]

    # santa get scored
    score_board[santa_num] += D

    # santa get stunned
    present_santa.stun += 1

    # santa moved
    nsr,nsc = pr-sdr*D,pc-sdc*D
    present_santa.row = nsr
    present_santa.col = nsc

    # when next destination is in range
    if 0 <= nsr < N and 0 <= nsc < N:
        # when there is another santa
        if board[nsr][nsc]:
            board[nsr][nsc].append(santa_num)
            splash(nsr, nsc, -sdr, -sdc)
        # when there is nothing
        else:
            board[nsr][nsc].append(santa_num)
    # when santa become out of range
    else:
        alived.pop(santa_num)

def splash(pr,pc,dr,dc):
    santa_num = board[pr][pc].popleft()
    present_santa = alived[santa_num]
    nsr,nsc = pr+dr,pc+dc
    present_santa.row = nsr
    present_santa.col = nsc
    # when next destination is in range
    if 0 <= nsr < N and 0 <= nsc < N:
        # when there is another santa
        if board[nsr][nsc]:
            board[nsr][nsc].append(santa_num)
            splash(nsr,nsc,dr,dc)
        # when there is nothing
        else:
            board[nsr][nsc].append(santa_num)
    # when santa become out of range
    else:
        alived.pop(santa_num)

# initialize
score_board = [0]*(P)
alived = {}
board = [[deque() for i in range(N)] for j in range(N)]

rr,rc = map(lambda x:int(x)-1,sys.stdin.readline().split())
board[rr][rc].append(-1)

for _ in range(P):
    p_n,sr,sc = map(lambda x:int(x)-1,sys.stdin.readline().split())
    santa = Santa(p_n,sr,sc)
    board[sr][sc].append(p_n)
    alived[p_n] = santa

# simulation
while M > 0 and alived:
    rr, rc = rudolph_move(rr,rc)

    for key in sorted(alived.keys()):
        santa_move(key,rr,rc)

    M -= 1
    for s_num in alived.keys():
        score_board[s_num] += 1

print(*score_board)