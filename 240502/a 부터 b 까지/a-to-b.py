a,b = map(int,input().split())

ans = []
while a <= b:
    ans.append(a)
    if a % 2: a *= 2
    else: a += 3

print(*ans)