N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(N-2):
        count = 0
        for row in range(3):
            for col in range(3):
                count += board[row+i][col+j]
        ans = max(ans,count)

print(ans)