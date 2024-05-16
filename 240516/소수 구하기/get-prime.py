n = int(input())

base = []

for num in range(1,n+1):
    temp = 0
    for i in range(1,num):
        if num%i == 0: temp += 1
    if temp == 1: base.append(num)

print(*base)