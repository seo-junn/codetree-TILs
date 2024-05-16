a,b = map(int,input().split())

for i in range(2,10,2):
    for j in range(b,a,-1):
        print(f'{j} * {i} = {j*i}',end=' / ')
    print(f'{a} * {i} = {a*i}')