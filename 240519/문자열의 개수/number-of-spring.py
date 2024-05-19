base = []
count = 0

while True:
    line = input()
    if line == '0': break
    count += 1
    if count%2: base.append(line)

print(count)
for line in base: print(line)