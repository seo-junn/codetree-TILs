base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
idx = 0

for i in range(N):
    print('  '*i,end='')
    for _ in range(N-i):
        print(base[idx],end=' ')
        idx = (idx+1)%26
    print()