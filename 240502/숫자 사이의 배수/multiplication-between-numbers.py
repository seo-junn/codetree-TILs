a,b = map(int,input().split())

total = 0
count = 0
for num in range(a,b+1):
    if num%5 == 0 or num%7 == 0:
        total += num
        count += 1

print(total,'%.1f'%(total/count))