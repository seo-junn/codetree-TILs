n,m = map(int,input().split())

base = [[0]*m for _ in range(n)]

num = 0
for diagonal in range(n+m-1):
    for row in range(n):
        col = diagonal-row
        if 0 <= row < n and 0 <= col < m:
            num += 1
            base[row][col] = num

for line in base: print(*line)