count = 0

for _ in range(3):
    f,c = input().split()
    c = int(c)
    if f == 'Y' and c >= 37: count += 1

print('E' if count >= 2 else 'N')