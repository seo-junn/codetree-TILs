ans = 0
a,b = map(int,input().split())
if a > b: a,b = b,a
for num in range(a,b+1):
    if num%5 == 0: ans += num

print(ans)