line = list(input())
f,s = line[:2]
for i in range(len(line)):
    if line[i] == f: line[i] = s
    elif line[i] == s: line[i] = f
print(''.join(line))