n,m = map(int,input().split())
live = list(map(int,input().split()))

coverage = 2*m+1

end = 0
count = 0

while end < n:
    if live[end] == 0: end += 1
    else:
        end += coverage
        count += 1

print(count)