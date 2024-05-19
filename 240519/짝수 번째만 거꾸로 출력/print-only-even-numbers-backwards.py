ans = ''
line = input()

for i in range(len(line)):
    if i%2: ans += line[i]

print(ans[::-1])