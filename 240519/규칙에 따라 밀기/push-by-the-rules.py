line = input()
for c in input():
    if c == 'L': line = line[1:] + line[0]
    else: line = line[-1] + line[:-1]
print(line)