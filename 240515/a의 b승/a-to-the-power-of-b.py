a,b = map(int,input().split())

ans = 1
for _ in range(b):
    ans *= a

print(ans)