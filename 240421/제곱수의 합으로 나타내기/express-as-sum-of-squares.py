from itertools import combinations

n = int(input())
found = False

for i in range(1,5):
    for item in combinations(range(1,71),i):
        temp = 0
        for num in item:
            temp += num**2
        if temp == n:
            print(len(item))
            found = True
            break
    if found: break