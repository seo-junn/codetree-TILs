n = int(input())

for i in range(1,n+1):
    if i%2: print('*')
    else: print('*'+' *'*(i-1))