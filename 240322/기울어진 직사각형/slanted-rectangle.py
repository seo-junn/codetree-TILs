import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0
for row in range(n):
    for col in range(n):
        for odd in range(1,n):
            for even in range(1,n):
                temp = 0
                pr,pc = row,col
                fail = False
                for _ in range(odd):
                    nr,nc = pr-1,pc+1
                    if 0 <= nr < n and 0 <= nc < n:
                        temp += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        temp = 0
                        fail = True
                        break
                
                if fail: continue

                for _ in range(even):
                    nr,nc = pr-1,pc-1
                    if 0 <= nr < n and 0 <= nc < n:
                        temp += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        temp = 0
                        fail = True
                        break
                
                if fail: continue

                for _ in range(odd):
                    nr,nc = pr+1,pc-1
                    if 0 <= nr < n and 0 <= nc < n:
                        temp += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        temp = 0
                        fail = True
                        break
                
                if fail: continue

                for _ in range(even):
                    nr,nc = pr+1,pc+1
                    if 0 <= nr < n and 0 <= nc < n:
                        temp += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        temp = 0
                        fail = True
                        break
                
                if fail: continue

                ans = max(ans,temp)

print(ans)