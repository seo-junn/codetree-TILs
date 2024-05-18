base = [[1]*5 for _ in range(5)]

for i in range(1,5):
    for j in range(1,5):
        base[i][j] = base[i-1][j] + base[i][j-1]

for line in base: print(*line)