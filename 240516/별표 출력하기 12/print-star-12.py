n = int(input())

if n == 1:
    print('*')
    exit(0)

base = ['*']

for i in range(2,n+1):
    if i%2:
        base.append('*')
    else:
        base.append('*'*i)

row = n if n%2 == 0 else n-1

for _ in range(row):
    line = ''
    if _ < len(base[0]): line += '*'
    else: line += ' '

    for i in range(1,n-1):
        if _ < len(base[i]): line += ' *'
        else: line += '  '
    
    if _ < len(base[-1]): line += ' *'
    
    print(line)