a,b = map(int,input().split())
if a > b: a,b = b,a

total = 0
for num in range(a,b+1):
    if num%2 == 0: total += num

print(total)