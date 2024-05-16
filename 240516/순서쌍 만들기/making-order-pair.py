n = int(input())

for r in range(n,0,-1):
    for c in range(n,0,-1):
        print(f'({r},{c})',end=' ')
    print()