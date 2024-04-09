n = int(input())
for i in range(2*n):
    if i%2 == 0:
        line = '* '*(n-(i//2)) 
        print(line[:-1])
    else:
        line = '* '*((i+1)//2)
        print(line[:-1])