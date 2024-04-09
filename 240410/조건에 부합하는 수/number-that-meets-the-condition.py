a = int(input())

ans = []
for num in range(1,a+1):
    if (not (num%2==0 and num%4)) and (not (num//8)%2 == 0) and (not num%7 < 4): ans.append(num)

print(*ans)