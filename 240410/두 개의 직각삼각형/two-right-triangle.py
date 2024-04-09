n = int(input())
for i in range(n):
    line = '*'*(n-i)+' '*i
    line = line+line[::-1]
    print(line)