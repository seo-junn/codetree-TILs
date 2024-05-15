a,b,c = map(int,input().split())

find = False
for num in range(a,b+1):
    if num%c == 0:
        find = True
        break

print("YES" if find else "NO")