n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

ans = -(10**7)

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1,n):
            for c2 in range(c1,m):
                for r3 in range(r1,n):
                    if r2 >= r3:
                        for c3 in range(c2+1,m):
                            for r4 in range(r3,n):
                                for c4 in range(c3,n):
                                    temp = 0
                                    for r in range(r1,r2+1):
                                        for c in range(c1,c2+1):
                                            temp += board[r][c]
                                    for r in range(r3,r4+1):
                                        for c in range(c3,c4+1):
                                            temp += board[r][c]
                                    ans = max(ans,temp)
                    else:
                        for c3 in range(m):
                            for r4 in range(r3,n):
                                for c4 in range(c3,n):
                                    temp = 0
                                    for r in range(r1,r2+1):
                                        for c in range(c1,c2+1):
                                            temp += board[r][c]
                                    for r in range(r3,r4+1):
                                        for c in range(c3,c4+1):
                                            temp += board[r][c]
                                    ans = max(ans,temp)

print(ans)