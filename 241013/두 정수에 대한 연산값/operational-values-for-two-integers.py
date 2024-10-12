def modify(a,b):
    if a < b:
        return a*2, b+25
    else:
        return a+25, b*2

a,b = map(int,input().split())
a,b = modify(a,b)
print(a,b)