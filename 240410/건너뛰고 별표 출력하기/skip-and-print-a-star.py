n = int(input())
for i in range(1,n):
    print('*'*i)
    print()
print('*'*n)
for i in range(n-1,0,-1):
    print()
    print('*'*i)