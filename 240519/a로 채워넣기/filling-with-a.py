line = list(input())
line[1],line[-2] = 'a','a'
print(''.join(line))