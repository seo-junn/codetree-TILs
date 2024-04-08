import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0
for row in range(2,n):
    for col in range(1,n-1):
        for odd in range(1,n):
            for even in range(1,n):
                val = 0
                pr,pc = row,col
                fail = False
                for i in range(odd):
                    nr,nc = pr-1,pc+1
                    if 0 <= nr < n and 0 <= nc < n:
                        val += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        fail = True
                        break
                if fail: break

                for i in range(even):
                    nr,nc = pr-1,pc-1
                    if 0 <= nr < n and 0 <= nc < n:
                        val += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        fail = True
                        break
                if fail: continue

                for i in range(odd):
                    nr,nc = pr+1,pc-1
                    if 0 <= nr < n and 0 <= nc < n:
                        val += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        fail = True
                        break
                if fail: break

                for i in range(even):
                    nr,nc = pr+1,pc+1
                    if 0 <= nr < n and 0 <= nc < n:
                        val += board[nr][nc]
                        pr,pc = nr,nc
                    else:
                        fail = True
                        break
                if fail: continue
                
                ans = max(ans,val)
print(ans)