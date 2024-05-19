line = input()
print(line)
for i in range(len(line)):
    line = line[-1] + line[:-1]
    print(line)