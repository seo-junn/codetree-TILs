c3,c5 = 0,0

for _ in range(10):
    num = int(input())
    if num%3 == 0: c3 += 1
    if num%5 == 0: c5 += 1

print(c3,c5)