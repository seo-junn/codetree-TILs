a,b = map(int,input().split())

ans = 1
for num in range(1,b+1):
    if num%a == 0:
        ans *= num
print(ans)