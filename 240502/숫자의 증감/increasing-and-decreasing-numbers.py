c,n = input().split()

if c == 'A':
    print(*list(range(1,int(n)+1)))
else:
    print(*list(range(int(n),0,-1)))