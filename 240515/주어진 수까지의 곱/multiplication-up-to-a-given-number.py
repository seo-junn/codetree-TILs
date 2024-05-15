ans = 1

a,b = map(int,input().split())

for i in range(a,b+1):
    ans *= i

print(ans)