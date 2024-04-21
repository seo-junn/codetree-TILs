n = int(input())

count = 10**9

for five in range(n//5+1):
    if (n-five*5)%3 == 0:
        temp = five + (n-five*5)//3
        if temp < count:
            count = temp

print(count if count < 10**9 else -1)