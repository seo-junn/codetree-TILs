import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def search(row,col):
    max_val = 0
    for depth in range(2,row+1):
        for ur in range(1,min(depth,n-col)):
            ul = depth-ur
            val = 0
            pr,pc = row,col
            for i in range(ur):
                nr,nc = pr-1,pc+1
                pr,pc = nr,nc
                val += board[pr][pc]
            for i in range(ul):
                nr,nc = pr-1,pc-1
                pr,pc = nr,nc
                val += board[pr][pc]
            for i in range(ur):
                nr,nc = pr+1,pc-1
                pr,pc = nr,nc
                val += board[pr][pc]
            for i in range(ul):
                nr,nc = pr+1,pc+1
                pr,pc = nr,nc
                val += board[pr][pc]
            max_val = max(max_val,val)
    return max_val

ans = 0
for row in range(2,n):
    for col in range(1,n-1):
        ans = max(ans,search(row,col))

print(ans)