base = 'LEBROS'
c = input()
idx = -1

for i in range(6):
    if base[i] == c:
        idx = i

print(idx if idx != -1 else "None")