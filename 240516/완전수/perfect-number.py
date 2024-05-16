s,e = map(int,input().split())

count = 0
for n in range(s,e+1):
    base = 0
    for i in range(1,n):
        if n%i == 0: base += i
    
    if base == n: count += 1

print(count)