import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, M = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def size_check():
    count = 0
    for i in range(N):
        for j in range(M):
            count += board[i][j]
    return count

def melting():
    q = deque()
    q.append((0,0))
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True

    while q:
        pr,pc = q.popleft()
        for i in range(4):
            nr,nc = pr+dr[i],pc+dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 0:
                    q.append((nr,nc))
                else:
                    board[nr][nc] = 0

time = 0
ice_size = size_check()
while True:
    melting()
    time += 1
    temp = size_check()
    if temp == 0: break
    ice_size = temp

print(time, ice_size)