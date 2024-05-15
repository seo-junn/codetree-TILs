n = int(input())

ans = []
for num in range(1,n+1):
    if num%2 == 0: continue
    elif num%10 == 5: continue
    elif num%3 == 0 and num%9 != 0: continue
    ans.append(num)

print(*ans)