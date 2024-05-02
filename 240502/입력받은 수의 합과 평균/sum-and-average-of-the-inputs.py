total = 0
n = int(input())

for _ in range(n):
    num = int(input())
    total += num

print(total,f'{total/n:.1f}')