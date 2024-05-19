n = int(input())

base = [[1]*n for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        base[i][j] = base[i-1][j-1] + base[i-1][j] + base[i][j-1]

for line in base: print(*line)