base = [list(map(int,input().split())) for _ in range(2)]

print(f'{sum(base[0])/4:.1f} {sum(base[1])/4:.1f}')
for i in range(4):
    print(f'{(base[0][i]+base[1][i])/2:.1f}',end=' ')
print()
print(f'{(sum(base[0])+sum(base[1]))/8:.1f}')