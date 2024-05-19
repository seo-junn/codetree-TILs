line = input()

idx = -1
for i in range(len(line)):
    if line[i] == 'e':
        idx = i
        break

print(line[:i]+line[i+1:])