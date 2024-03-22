n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

ans = -(10**7)

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1,n):
            for c2 in range(c1,m):
                for r3 in range(n):
                    for c3 in range(m):
                        for r4 in range(r3,n):
                            for c4 in range(c3,n):
                                if r1 <= r3 <= r2 or r1 <= r4 <= r2 or (c3 <= c1 <= c4 and c3 <= c2 <= c4):
                                    if c1 <= c3 <= c2 or c1 <= c4 <= c2 or (c3 <= c1 <= c4 and c3 <= c2 <= c4): continue
                                    temp = 0
                                    for r in range(r1,r2+1):
                                        for c in range(c1,c2+1):
                                            temp += board[r][c]
                                    for r in range(r3,r4+1):
                                        for c in range(c3,c4+1):
                                            temp += board[r][c]
                                    ans = max(ans,temp)
                                else:
                                    temp = 0
                                    for r in range(r1,r2+1):
                                        for c in range(c1,c2+1):
                                            temp += board[r][c]
                                    for r in range(r3,r4+1):
                                        for c in range(c3,c4+1):
                                            temp += board[r][c]
                                    ans = max(ans,temp)


print(ans)