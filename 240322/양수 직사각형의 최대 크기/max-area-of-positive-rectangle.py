n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

ans = -1
for r1 in range(n):
    for c1 in range(n):
        for r2 in range(r1,n):
            for c2 in range(c1,n):
                pos = True
                for r in range(r1,r2+1):
                    for c in range(c1,c2+1):
                        if board[r][c] <= 0:
                            pos = False
                if pos:
                    ans = max(ans,(r2-r1+1)*(c2-c1+1))

print(ans)