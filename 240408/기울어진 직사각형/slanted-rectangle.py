import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def search(row,col,odd,even):
    drs,dcs = [-1,-1,1,1],[1,-1,-1,1]
    moves = [odd,even,odd,even]

    val = 0

    for dr,dc,move in zip(drs,dcs,moves):
        for _ in range(move):
            row,col = row+dr,col+dc
            if 0 <= row < n and 0 <= col < n:
                val += board[row][col]
            else:
                return 0
    return val

ans = 0
for row in range(2,n):
    for col in range(1,n-1):
        for odd in range(1,n):
            for even in range(1,n):
                ans = max(ans,search(row,col,odd,even))
print(ans)