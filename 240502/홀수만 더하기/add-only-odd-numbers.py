count = 0
for _ in range(int(input())):
    num = int(input())
    if num%2 and num%3 == 0: count += 1

print(count)