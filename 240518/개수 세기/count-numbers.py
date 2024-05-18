n,m = map(int,input().split())
count = 0

for num in map(int,input().split()):
    if num == m: count += 1

print(count)