n = int(input())
cnt = 1

for i in range(n):
    print('  '*i,end='')
    for _ in range(n-i):
        print(cnt,end=' ')
        cnt += 1
        if cnt == 10: cnt = 1
    print()