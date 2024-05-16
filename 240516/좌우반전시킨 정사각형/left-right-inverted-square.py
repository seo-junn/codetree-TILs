n = int(input())

base = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        base[i][j] = (i+1)*(j+1)

for line in base: print(*line[::-1])