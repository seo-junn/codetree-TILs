base = [0]*7

for num in map(int,input().split()):
    base[num] += 1

for i in range(1,7):
    print(f"{i} - {base[i]}")