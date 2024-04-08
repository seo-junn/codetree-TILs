import sys

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

b1 = [[1,0],
      [1,1]]

b2 = [[1,1],
      [1,0]]

b3 = [[1,1],
      [0,1]]

b4 = [[0,1],
      [1,1]]

max_sum = 0

for row in range(n-1):
    for col in range(m-1):
        val1,val2,val3,val4 = 0,0,0,0
        for i in range(2):
            for j in range(2):
                val1 += board[row+i][col+j]*b1[i][j]
                val2 += board[row+i][col+j]*b2[i][j]
                val3 += board[row+i][col+j]*b3[i][j]
                val4 += board[row+i][col+j]*b4[i][j]
        max_sum = max(max_sum,val1,val2,val3,val4)

for row in range(n):
    for col in range(m-2):
        val = board[row][col]+board[row][col+1]+board[row][col+2]
        max_sum = max(max_sum,val)

for row in range(n-2):
    for col in range(m):
        val = board[row][col]+board[row+1][col]+board[row+2][col]
        max_sum = max(max_sum,val)

print(max_sum)