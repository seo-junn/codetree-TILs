base = [0]*10

n = int(input())
for num in map(int,input().split()):
    base[num] += 1

for i in range(1,10):
    print(base[i])