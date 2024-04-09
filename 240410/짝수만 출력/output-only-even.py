a,b = map(int,input().split())
ans = []
num = a
while num <= b:
    if num%2 == 0: ans.append(num)
    num += 1

print(*ans)