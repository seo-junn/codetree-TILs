n = int(input())

find = False
for i in range(2,n):
    if n%i == 0:
        find = True
        break

print('C' if find else 'P')