n = int(input())

base = [[0]*n for _ in range(n)]
base[0][0] = 11

for i in range(1,n):
    base[0][i] = base[0][i-1] + 2

for i in range(1,n):
    for j in range(n):
        base[i][j] = base[i-1][j] + 2

for line in base: print(*line)