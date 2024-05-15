a,b,c = map(int,input().split())

exist = False
for i in range(a,b+1):
    if i%c == 0:
        exist = True
        break

print("NO" if exist else "YES")