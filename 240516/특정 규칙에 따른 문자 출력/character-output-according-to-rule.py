n = int(input())

for i in range(1,n):
    print('  '*(n-i)+'@'+' @'*(i-1))
for i in range(n,0,-1):
    print('@'+' @'*(i-1))