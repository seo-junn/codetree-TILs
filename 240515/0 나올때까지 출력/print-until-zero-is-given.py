stack = []

while True:
    n = int(input())
    if n == 0: break
    stack.append(n)

for num in stack:
    print(num)