base = [0]*10

for num in map(int,input().split()):
    if num == 0: break
    base[num//10] += 1

for i in range(1,10):
    print(f"{i} - {base[i]}")