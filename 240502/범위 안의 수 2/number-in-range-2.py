total = 0
count = 0

for _ in range(10):
    num = int(input())
    if 0 <= num <= 200:
        total += num
        count += 1

print(total,f'{total/count:.1f}')