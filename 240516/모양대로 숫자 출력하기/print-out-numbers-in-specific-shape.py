n = int(input())

for i in range(n,0,-1):
    print('  '*(n-i) + ' '.join(list(map(str,range(i,0,-1)))))