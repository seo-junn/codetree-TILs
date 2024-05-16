base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx = 0
n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print(base[idx],end='')
        idx = (idx+1)%26
    print()