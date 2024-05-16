s,e = map(int,input().split())

count = 0
for n in range(s,e+1):
    temp_count = 0
    for i in range(1,n):
        if n%i == 0: temp_count += 1
    if temp_count == 2: count += 1

print(count)