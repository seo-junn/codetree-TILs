base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
idx = 0

for i in range(n):
    for j in range(n):
        print(base[idx],end='')
        idx = (idx+1)%26
    print()