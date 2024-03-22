line = input().strip()

count = 0
for i in range(len(line)-1):
    if line[i] == '(' and line[i+1] == '(':
        for j in range(i+2,len(line)-1):
            if line[j] == ')' and line[j+1] == ')':
                count += 1

print(count)