a,b,c = sorted(map(int,input().split()))

if b-a == c-b == 1:
    print(0)
elif b-a == 1:
    if c-b == 2: print(1)
    else: print(2)
elif c-b == 1:
    if b-a == 2: print(1)
    else: print(2)
else:
    print(2)