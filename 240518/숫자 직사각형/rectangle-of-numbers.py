n,m = map(int,input().split())

base = [[0]*m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        num += 1
        base[i][j] = num

for line in base: print(*line)