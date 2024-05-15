count = 0

while True:
    n = int(input())
    if n%2 == 0:
        print(n//2)
        count += 1
        if count == 3: break