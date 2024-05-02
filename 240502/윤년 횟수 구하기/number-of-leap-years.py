count = 0
for year in range(1,int(input())+1):
    if year%400 == 0: count += 1
    elif year%100 == 0: continue
    elif year%4 == 0: count += 1

print(count)