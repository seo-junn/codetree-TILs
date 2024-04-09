b,a = map(int,input().split())
ans = []
num = b
while num >= a:
    if num%2 == 0: ans.append(num)
    num -= 1

print(*ans)