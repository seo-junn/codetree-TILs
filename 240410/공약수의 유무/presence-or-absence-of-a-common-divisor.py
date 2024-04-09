a,b = map(int,input().split())
ans = 0
for num in range(a,b+1):
    if 1920%num == 0 and 2880%num == 0:
        ans = 1
        break

print(ans)