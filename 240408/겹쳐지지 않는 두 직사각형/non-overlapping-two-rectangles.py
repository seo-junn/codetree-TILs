import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
max_val = -sys.maxsize

def search(r1,r2,c1,c2):
    res = -sys.maxsize
    for rr1 in range(n):
        for rr2 in range(rr1,n):
            if rr2 < r1 or rr1 > r2:
                for cc1 in range(m):
                    for cc2 in range(cc1,m):
                        temp = 0
                        for row in range(rr1,rr2+1):
                            for col in range(cc1,cc2+1):
                                temp += board[row][col]
                        res = max(res,temp)
            else:
                for cc1 in range(c1):
                    for cc2 in range(cc1,c1):
                        temp = 0
                        for row in range(rr1,rr2+1):
                            for col in range(cc1,cc2+1):
                                temp += board[row][col]
                        res = max(res,temp)
                for cc1 in range(c2+1,m):
                    for cc2 in range(cc1,m):
                        temp = 0
                        for row in range(rr1,rr2+1):
                            for col in range(cc1,cc2+1):
                                temp += board[row][col]
                        res = max(res,temp)
    return res

for r1 in range(n):
    for r2 in range(r1,n):
        for c1 in range(m):
            for c2 in range(c1,m):
                base = 0
                for row in range(r1,r2+1):
                    for col in range(c1,c2+1):
                        base += board[row][col]
                max_val = max(max_val,base+search(r1,r2,c1,c2))

print(max_val)