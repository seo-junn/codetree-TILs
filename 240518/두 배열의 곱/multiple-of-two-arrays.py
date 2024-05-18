A = [list(map(int,input().split())) for _ in range(3)]
_ = input()
B = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        A[i][j] *= B[i][j]

for line in A: print(*line)