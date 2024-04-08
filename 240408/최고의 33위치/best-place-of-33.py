import sys

N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

max_count = 0
for row in range(N-2):
    for col in range(N-2):
        count = 0
        for i in range(3):
            for j in range(3):
                count += board[row+i][col+j]
        max_count = max(max_count,count)

print(max_count)