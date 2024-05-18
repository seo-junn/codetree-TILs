base = [0]*4

for _ in range(3):
    cold, temper = input().split()
    temper = int(temper)
    if cold == 'Y' and temper >= 37: base[0] += 1
    elif cold != 'Y' and temper >= 37: base[1] += 1
    elif cold == 'Y' and temper < 37: base[2] += 1
    else: base[3] += 1

print(*base,'E' if base[0] >= 2 else '')