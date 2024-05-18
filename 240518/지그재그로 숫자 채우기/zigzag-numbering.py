n,m = map(int,input().split())

base = [[0]*m for _ in range(n)]
num = 0
for col in range(m):
    if col%2 == 0:
        for row in range(n):
            base[row][col] = num
            num += 1
    else:
        for row in range(n-1,-1,-1):
            base[row][col] = num
            num += 1

for line in base: print(*line)