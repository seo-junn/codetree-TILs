base = [0]*11

for score in map(int,input().split()):
    if score == 0: break
    base[score//10] += 1

for i in range(10,0,-1):
    print(f"{i}0 - {base[i]}")