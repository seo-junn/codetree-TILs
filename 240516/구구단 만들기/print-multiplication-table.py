a,b = map(int,input().split())

for i in range(1,10):
    for j in range(b,a,-2):
        print(f'{j} * {i} = {j*i}',end=' / ')
    print(f'{a} * {i} = {a*i}')