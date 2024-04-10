import sys

base = set()
n = int(sys.stdin.readline())

for _ in range(n):
    command, x = sys.stdin.readline().split()
    x = int(x)

    if command == 'add':
        base.add(x)
    elif command == 'remove':
        base.remove(x)
    else:
        print("true" if x in base else "false")