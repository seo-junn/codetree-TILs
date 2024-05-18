n = int(input())

base = [[0]*n for _ in range(n)]

num = 0
for col in range(n-1,-1,-1):
    if col%2 == (n-1)%2:
        for row in range(n-1,-1,-1):
            num += 1
            base[row][col] = num
    else:
        for row in range(n):
            num += 1
            base[row][col] = num

for line in base: print(*line)