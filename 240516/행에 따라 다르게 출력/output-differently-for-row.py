n = int(input())

base = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    if i%2 == 0: step = 1
    else: step = 2
    for j in range(n):
        cnt += step
        print(cnt,end=' ')
    print()