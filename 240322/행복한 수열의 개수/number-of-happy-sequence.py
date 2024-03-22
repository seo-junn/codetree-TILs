import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

if m == 1:
    print(2*n)
    exit(0)

count = 0
for row in range(n):
    temp = 1
    for i in range(1,n):
        if board[row][i] == board[row][i-1]:
            temp += 1
        else:
            temp = 1
        if temp == m:
            count += 1
            break

for col in range(n):
    temp = 1
    for i in range(1,n):
        if board[i][col] == board[i-1][col]:
            temp += 1
        else:
            temp = 1
        if temp == m:
            count += 1
            break

print(count)