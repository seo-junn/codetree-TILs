N = int(input())

count = 0
while N != 1:
    if N%2:
        N = N*3+1
    else:
        N //= 2
    count += 1

print(count)