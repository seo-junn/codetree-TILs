n = int(input())

for i in range(n,0,-1):
    print('*'*i + (' '+'*'*i)*(i-1))