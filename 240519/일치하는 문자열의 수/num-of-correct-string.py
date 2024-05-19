count = 0
n,A = input().split()
for _ in range(int(n)):
    if input() == A: count += 1
print(count)