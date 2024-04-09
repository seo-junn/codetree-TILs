n = int(input())

count = 0
denom = 1
while n > 1:
    n /= denom
    denom += 1
    count += 1

print(count)