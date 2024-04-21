f,c = input().split()
c = int(c)

count = 0
if f == 'Y' and c >= 37: count += 1

print('E' if count >= 2 else 'N')