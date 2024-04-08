import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = -1

for r1 in range(n):
    for r2 in range(r1,n):
        for c1 in range(m):
            for c2 in range(c1,m):
                count = 0
                positive = True
                for row in range(r1,r2+1):
                    for col in range(c1,c2+1):
                        count += 1
                        if board[row][col] <= 0:
                            positive = False
                            break
                    if not positive: break
                if positive: ans = max(ans,count)

print(ans)