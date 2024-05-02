count = [0,0,0]

for day in range(1,int(input())+1):
    if day%12 == 0: count[2] += 1
    elif day%3 == 0: count[1] += 1
    elif day%2 == 0: count[0] += 1

print(*count)