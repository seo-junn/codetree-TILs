n = int(input())

present = 0
for i in range(1,101):
    present += i
    if present >= n:
        print(i)
        break