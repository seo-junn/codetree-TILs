a,b = map(int,input().split())

remainder = [0]*b

while a > 1:
    remainder[a%b] += 1
    a //= b

ans = 0
for n in remainder: ans += n**2

print(ans)