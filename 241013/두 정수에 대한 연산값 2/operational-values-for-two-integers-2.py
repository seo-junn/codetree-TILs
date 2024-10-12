def modify(a,b):
    if a < b:
        return a+10, b*2
    else:
        return a*2, b+10

a,b = map(int,input().split())
a,b = modify(a,b)

print(a,b)