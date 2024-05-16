n = int(input())

for i in range(n):
    if i%2:
        print(''.join(list(map(str,range(n,0,-1)))))
    else:
        print(''.join(list(map(str,range(1,n+1)))))