for _ in range(int(input())):
    a,b = map(int,input().split())
    base = 0
    for n in range(a,b+1):
        if n%2 == 0: base += n
    print(base)