import sys
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def can_move(knight_num,direct):
    if knight_num not in alived:
        return res, set()
    q = deque()
    moved = set()
    pr,pc,ph,pw,pk,pd = alived[knight_num]
    moved.add(knight_num)
    for ppr in range(ph):
        for ppc in range(pw):
            q.append((pr+ppr,pc+ppc))

    cache = [[0]*L for _ in range(L)]
    while q:
        pr,pc = q.popleft()
        nr,nc = pr+dr[direct],pc+dc[direct]
        if 0 <= nr < L and 0 <= nc < L and cache[nr][nc] == 0:
            cache[nr][nc] += 1
            if board[nr][nc] == 2:
                return False, moved
            else:
                if position[nr][nc] and position[nr][nc][0] not in moved:
                    moved.add(position[nr][nc][0])
                    r,c,h,w,k,pd = alived[position[nr][nc][0]]
                    for i in range(h):
                        for j in range(w):
                            q.append((r+i,c+j))
        else:
            return False, moved

    return True, moved

def move_knights(moved_knights,direct,f_knight):
    for k_num in moved_knights:
        if k_num in alived:
            r,c,h,w,k,d = alived[k_num]
            nr,nc = r+dr[direct],c+dc[direct]

            # calculate damage
            damage = 0
            for rr in range(h):
                for cc in range(w):
                    if board[nr+rr][nc+cc]: damage += 1
            if k_num != f_knight:
                d += damage

            for rr in range(h):
                for cc in range(w):
                    position[r + rr][c + cc].popleft()
            # when knight died
            if k <= d:
                alived.pop(k_num)
            # when knight alived
            else:
                for rr in range(h):
                    for cc in range(w):
                        position[nr+rr][nc+cc].append(k_num)
                alived[k_num] = (nr,nc,h,w,k,d)


L,N,Q = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(L)]

position = [[deque() for i in range(L)] for j in range(L)]
alived = {}

for i in range(N):
    r,c,h,w,k = map(int,sys.stdin.readline().split())
    r,c = r-1,c-1
    alived[i] = (r,c,h,w,k,0)
    for rr in range(h):
        for cc in range(w):
            position[r+rr][c+cc].append(i)

for _ in range(Q):
    num,direct = map(int,sys.stdin.readline().split())
    num -= 1
    res,moved = can_move(num,direct)
    if res:
        move_knights(moved,direct,num)

total_damage = 0
for r,c,h,w,k,d in alived.values():
    total_damage += d

print(total_damage)