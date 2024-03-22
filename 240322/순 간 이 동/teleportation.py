A, B, x, y = map(int,input().split())

c1 = abs(A-B)
c2 = abs(A-x)+abs(y-B)
c3 = abs(A-y)+abs(x-B)

print(min(c1,c2,c3))