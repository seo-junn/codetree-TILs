count = 0
n = int(input())

while n < 1000:
    if n%2:
        n = n*2+2
    else:
        n = n*3+1
    count += 1

print(count)